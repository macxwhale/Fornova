import json
import re

import requests
from bs4 import BeautifulSoup

url =  "https://www.qantas.com/hotels/properties/18482?adults=2&checkIn=2024-01-26&checkOut=2024-01-27&children=0&infants=0&location=London%2C%20England%2C%20United%20Kingdom&page=1&payWith=cash&searchType=list&sortBy=popularity"

page_to_scrape = requests.get(url)
#print(page_to_scrape.status_code)

soup = BeautifulSoup(page_to_scrape.content, "html.parser")

script_tag = soup.find_all('script')[45].text.strip()


data = json.loads(script_tag)
print(data)



rates = []

for room_type in data['props']['pageProps']['initialState']['property']['property']['roomTypes']:
    room_name = room_type['name']
    rate_name = []
    no_of_guests = room_type['maxOccupantCount']
    cancel_policy = []
    price = []
    top_deal = []
    currency = []
    rates.append({"room_name": room_name, "rate_name": rate_name, "no_of_guests": no_of_guests, "cancel_policy": cancel_policy, "price": price, "top_deal": top_deal, "currency": currency })

result_json = json.dumps({"rates": rates}, indent=2)

print(result_json)













