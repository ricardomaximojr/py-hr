import json

def load(inventory_filename):
    with open(inventory_filename) as f:
        return json.load(f)
def dump(dest_filename, users_to_export_list):
    pass