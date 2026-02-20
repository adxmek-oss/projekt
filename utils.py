import ujson

def load_config():
    with open("configuration.txt") as f:
        return ujson.load(f)