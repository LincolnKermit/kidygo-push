import requests, json, bs4
from lib import config, remove_double

data_list = []
price_list = []

departure, arrival, is_transversal, delta = config.get_data()

endpoint = f"https://www.kidygo.fr/recherche/{departure}/{arrival}"
response = requests.get(endpoint)

# TODO : ADD WHILE TRUE WITH TIME SLEEP DELTA
# TODO : PARSE THE RESPONSE TO FILTER THE DATA
# TODO: SEND THE DATA BACK TO A ENDPOINT

element = bs4.BeautifulSoup(response.text, 'html.parser')
price = element.find_all('p', class_='price-annonce')
datetime = element.find_all('p', class_='date-annonce') 

for i in datetime:
    data_list.append(i.text)


for i in price:
    price_list.append(i.text)


remove_double(data_list)
remove_double(price_list)


for datetime in data_list:
    print(datetime)

for price in price_list:
    print(price)


for i in range(0, len(price_list), 2):
    print(f"index={i}: {price_list[i]}")