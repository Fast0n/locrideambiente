# Your Bot token (get it from BotFather)
TOKEN = 'TOKEN'

# Your Chat ID
CHAT_ID = "CHAT_ID"


# type
type_ = {
    "Vetro": "π· Vetro\n",
    "Carta e cartone": "π¦ Carta e Cartone\n",
    "Organico": "π Organico\n",
    "Sfalci e potature": "π Sfalci e potature\n",
    "Multimateriale": "πPlastica e Alluminio\n",
    "Indifferenziato": "πΌ Indifferenziato\n",
    "Ritiro ingombranti": "π Ingombranti\n",
    "Ingombranti": "π Ingombranti"
}


location = 'LOCATION'
id_ = {
    "bovalino": "13",
    "cariati": "36",
    "condofuri": "55",
    "grotteria": "17",
    "monasterace": "59",
    "palmi": "24",
    "san-luca": "45",
    "siderno": "38"
}

url = "{}{}{}".format(
    'https://www.locrideambientespa.it/comune-', location, '/')


# Request direct api
url_api = "{}{}".format(
    'https://www.locrideambientespa.it/wp/wp-admin/admin-ajax.php?action=get_wdtable&table_id=', id_[location])
payload_api = "draw=1&columns%5B0%5D%5Bdata%5D=0&columns%5B0%5D%5Bname%5D=wdt_ID&columns%5B0%5D%5Bsearchable%5D=true&columns%5B0%5D%5Borderable%5D=true&columns%5B0%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B0%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B1%5D%5Bdata%5D=1&columns%5B1%5D%5Bname%5D=rifiuti&columns%5B1%5D%5Bsearchable%5D=true&columns%5B1%5D%5Borderable%5D=false&columns%5B1%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B1%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B2%5D%5Bdata%5D=2&columns%5B2%5D%5Bname%5D=lunedi&columns%5B2%5D%5Bsearchable%5D=true&columns%5B2%5D%5Borderable%5D=true&columns%5B2%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B2%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B3%5D%5Bdata%5D=3&columns%5B3%5D%5Bname%5D=martedi&columns%5B3%5D%5Bsearchable%5D=true&columns%5B3%5D%5Borderable%5D=false&columns%5B3%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B3%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B4%5D%5Bdata%5D=4&columns%5B4%5D%5Bname%5D=mercoledi&columns%5B4%5D%5Bsearchable%5D=true&columns%5B4%5D%5Borderable%5D=false&columns%5B4%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B4%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B5%5D%5Bdata%5D=5&columns%5B5%5D%5Bname%5D=giovedi&columns%5B5%5D%5Bsearchable%5D=true&columns%5B5%5D%5Borderable%5D=false&columns%5B5%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B5%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B6%5D%5Bdata%5D=6&columns%5B6%5D%5Bname%5D=venerdi&columns%5B6%5D%5Bsearchable%5D=true&columns%5B6%5D%5Borderable%5D=false&columns%5B6%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B6%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B7%5D%5Bdata%5D=7&columns%5B7%5D%5Bname%5D=sabato&columns%5B7%5D%5Bsearchable%5D=true&columns%5B7%5D%5Borderable%5D=false&columns%5B7%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B7%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B8%5D%5Bdata%5D=8&columns%5B8%5D%5Bname%5D=domenica&columns%5B8%5D%5Bsearchable%5D=true&columns%5B8%5D%5Borderable%5D=false&columns%5B8%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B8%5D%5Bsearch%5D%5Bregex%5D=false&order%5B0%5D%5Bcolumn%5D=0&order%5B0%5D%5Bdir%5D=asc&start=0&length=10&search%5Bvalue%5D=&search%5Bregex%5D=false&wdtNonce="
headers_api = {
    'authority': 'www.locrideambientespa.it',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'x-requested-with': 'XMLHttpRequest',
    'origin': 'https://www.locrideambientespa.it',
    'referer': url
}


# bin
if int(url_api[-2:]) == 13 or int(url_api[-2:]) == 17 or int(url_api[-2:]) == 59:
    bin_ = {
        "Vetro": "π© _Cestello Verde_\n",
        "Carta e cartone": "β¬οΈ _Cestello Bianco_\n",
        "Organico": "π« _Cestello Marrone_\n",
        "Sfalci e potature": "π« _Cestello Marrone_\n",
        "Multimateriale": "π¦ _Cestello Blu_\n",
        "Indifferenziato": "β¬οΈ _Cestello Grigio_\n",
        "Ritiro ingombranti": ""
    }
elif int(url_api[-2:]) == 36 or int(url_api[-2:]) == 55 or int(url_api[-2:]) == 24 or int(url_api[-2:]) == 45 or int(url_api[-2:]) == 38:
    bin_ = {
        "Vetro": "π© _Cestello Verde_\n",
        "Carta e cartone": "π¦ _Cestello Blu_\n",
        "Organico": "π« _Cestello Marrone_\n",
        "Sfalci e potature": "π« _Cestello Marrone_\n",
        "Multimateriale": "π¨ _Cestello Giallo_\n",
        "Indifferenziato": "β¬οΈ _Cestello Grigio_\n",
        "Ritiro ingombranti": "",
        "Ingombranti": ""
    }
