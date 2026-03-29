import json

ID_FILE = "id_state.json"

def load_ids():
    with open(ID_FILE, "r") as f:
        return json.load(f)

def save_ids(data):
    with open(ID_FILE, "w") as f:
        json.dump(data, f, indent=4)

def generate_id(type):
    ids = load_ids()
    ids[type] += 1
    save_ids(ids)
    return ids[type]