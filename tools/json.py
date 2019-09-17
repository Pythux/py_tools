import json


def json_update(path, key, value):
    with open(path, 'r+') as f:
        data = json.load(f)
        data[key] = value
        f.seek(0)       # <--- should reset file position to the beginning.
        json.dump(data, f, indent=4)
        f.truncate()    # remove remaining part
