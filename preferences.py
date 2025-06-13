import json
import os

FILE = 'prefs.json'

def load():
    if not os.path.exists(FILE):
        return {}
    return json.load(open(FILE))

def save(data):
    with open(FILE, 'w') as f:
        json.dump(data, f, indent=2)

def add_topic(user_id, topic):
    prefs = load()
    prefs.setdefault(str(user_id), {'plus': [], 'minus': []})
    prefs[str(user_id)]['plus'].append(topic)
    save(prefs)

def remove_topic(user_id, topic):
    prefs = load()
    prefs.setdefault(str(user_id), {'plus': [], 'minus': []})
    if topic in prefs[str(user_id)]['plus']:
        prefs[str(user_id)]['plus'].remove(topic)
    prefs[str(user_id)]['minus'].append(topic)
    save(prefs)

def get_prefs(user_id):
    prefs = load().get(str(user_id), {'plus': [], 'minus': []})
    return prefs['plus'], prefs['minus']
