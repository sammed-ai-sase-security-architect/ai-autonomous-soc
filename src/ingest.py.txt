import json

def load_logs(path):
    with open(path) as f:
        return json.load(f)