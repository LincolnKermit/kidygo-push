import json

def remove_double(list_data):
    return list(set(list_data))


class config:
    with open('config.json') as f:
        data = json.load(f)
        def departure():
            return data['config']['departure']
        def arrival():
            return data['config']['arrival']
        def is_tranversal():
            return data['config']['is_transversal']
        def delta():
            return data['config']['delta']
