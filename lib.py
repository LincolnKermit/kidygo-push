import json

def remove_double(list_data):
    return list(set(list_data))


class config:
    def get_data():
        # get data from config.json
        with open('config.json') as f:
            data = json.load(f)
            departure = data['config']['departure']
            arrival = data['config']['arrival']
            is_transversal = data['config']['is_transversal']
            delta = data['config']['delta']
            return departure, arrival, is_transversal, delta