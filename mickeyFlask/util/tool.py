import json

def print_json(jsonObj):
    print(json.dumps(jsonObj, sort_keys=True, indent=4, ensure_ascii=False))