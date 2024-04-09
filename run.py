import logging
import time
from datetime import date, timedelta
import holidays
import requests
import schedule
from pid.decorator import pidfile
from telegram.ext import Updater

from settings import TOKEN, url_api

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

logger = logging.getLogger(__name__)


def job(bot, time):
    print(time)
    addDayDebug=0
    # get present day and add one day
    EndDate = date.today() + timedelta(days=2 + addDayDebug)
    EndDateHoly = date.today() + timedelta(days=1 + addDayDebug)
    it_holidays = holidays.country_holidays('IT', subdiv='RC')

    if EndDate.weekday() != 0 and not EndDateHoly in it_holidays:
        
        # Eseguo la richiesta GET al link fornito
        response = requests.get(url_api)

        # Estraggo il JSON dalla risposta
        json_data_array = response.json()

        # create the message to be sent on Telegram
        for json_data in json_data_array:
            waste = ''
            for json_data_data in json_data['data']:
                if json_data_data[EndDate.weekday()+1] == 0:
                    waste += f"{json_data['scheme_type'][json_data_data[1].capitalize()]}{json_data['scheme_bin'][json_data_data[1].capitalize()]}\n"

            message = f"*Buonasera { json_data['name']} 🌆*\n*E' arrivato il momento di portare fuori:*\n\n{waste} {json_data['desc']}"
            if time == json_data['time']:
                bot.send_message(chat_id=json_data['telegramid'], text=message,parse_mode="MarkdownV2")

                # print actualy date
                print(str(date.today()))
            


@ pidfile(pidname='/tmp/differenziata.pid')
def main():
    print("--- Starting Differenziata ---")
    # Setup bot
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    

    # Eseguire la richiesta GET per ottenere l'orario
    response = requests.get(url_api)
    json_data_array = response.json()

    # Eseguire la richiesta GET per ottenere l'orario
    response = requests.get(url_api)
    # Estraggo il JSON dalla risposta
    json_data_array = response.json()

    orari = []
    # create the message to be sent on Telegram
    for json_data in json_data_array:
        orari.append(json_data['time'])
    
    
    for orario in orari:
        schedule.every().day.at(orario).do(job, updater.bot, orario)

    while True:        
        schedule.run_pending()
        time.sleep(30)  # wait 30 seconds

    


if __name__ == "__main__":
    main()
