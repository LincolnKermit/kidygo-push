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


remove_double(data_list)

print(data_list)
