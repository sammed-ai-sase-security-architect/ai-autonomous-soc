import yaml

def load_mapping():
    with open("config/mitre_mapping.yaml") as f:
        return yaml.safe_load(f)

def map_mitre(action):
    mapping = load_mapping()

    if "login_fail" in action:
        return mapping["login_bruteforce"]

    return "unknown"