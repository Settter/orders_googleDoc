import requests

path = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()

# get relevant dollar to the ruble exchange rate
def get_rub_value(usd_value):
    print("search roubles course")
    return round(path['Valute']['USD']['Value']) * usd_value







