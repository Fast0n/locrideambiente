#!/usr/bin/env python3

import json
import logging
import time
from datetime import date, timedelta

import holidays
import requests
import schedule
from bs4 import BeautifulSoup
from pid.decorator import pidfile
from settings import (CHAT_ID, TOKEN, bin_, headers_api, location, payload_api,
                      type_, url, url_api)
from telegram.ext import Updater

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

logger = logging.getLogger(__name__)


def job(bot, addDayDebug=0):
    # get present day and add one day
    EndDate = date.today() + timedelta(days=2 + addDayDebug)

    # Get wdtNonce
    response_wdtNonce = requests.request(
        "GET", url
    )
    soup = BeautifulSoup(response_wdtNonce.text, features="html.parser")
    wdtNonceFrontendEdit = soup.find("input", {"id": "wdtNonceFrontendEdit"}).get(
        "value"
    )

    it_holidays = holidays.country_holidays('IT', subdiv='RC')

    if EndDate.weekday() != 0 and not EndDate in it_holidays:
        waste = ""
        response_api = requests.request(
            "POST",
            url_api,
            headers=headers_api,
            data=payload_api + wdtNonceFrontendEdit,
        )
        data = json.loads(response_api.text)

        # create the message to be sent on Telegram
        for a in range(len(data["data"])):
            for b in range(len(data["data"][a])):
                if b == EndDate.weekday() and data["data"][a][b + 1] != "":
                    waste += "*{}*{}\n".format(
                        type_[str(data["data"][a][1]).replace(
                            '*', '').capitalize()],
                        bin_[
                            str(data["data"][a][1]).replace('*', '').capitalize()],
                    )

        message = "*Buonasera {} 🌆*\n*E' arrivato il momento di portare fuori:*\n\n{}_Esporre dalle ore 21:00 alle ore 24:00_".format(
            location.replace('-', ' ').capitalize(), waste
        )

        # send the message on Telegram
        bot.send_message(chat_id=CHAT_ID, text=message,
                         parse_mode="MarkdownV2")

        # print actualy date
        print(str(date.today()))
    return


@ pidfile(pidname='/tmp/Locrideambiente.pid')
def main():
    print("--- Starting Locrideambiente ---")
    # Setup bot
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    schedule.every().day.at("21:00").do(dispatcher.run_async(job, updater.bot))

    while True:
        schedule.run_pending()
        time.sleep(30)  # wait 30 seconds


if __name__ == "__main__":
    main()
