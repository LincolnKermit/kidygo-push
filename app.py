import requests, json

class config:
    def get_data():
        # get data from config.json
        with open('config.json') as f:
            data = json.load(f)
            print(data)
            departure = data['config']['departure']
            arrival = data['config']['arrival']
            is_transversal = data['config']['is_transversal']
            delta = data['config']['delta']
            return departure, arrival, is_transversal, delta
        
departure, arrival, is_transversal, delta = config.get_data()

endpoint = f"https://www.kidygo.fr/recherche/{departure}/{arrival}"
response = requests.get(endpoint)
print(response.text)

# TODO : ADD WHILE TRUE WITH TIME SLEEP DELTA
# TODO : PARSE THE RESPONSE TO FILTER THE DATA
# TODO: SEND THE DATA BACK TO A ENDPOINT