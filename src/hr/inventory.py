import json

def load(inventory_filename):
    with open(inventory_filename) as f:
        return json.load(f)
        