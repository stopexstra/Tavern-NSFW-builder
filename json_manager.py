import json

TARGET_SECTIONS = [
    "enemyKnowledge",
    "events",
    "cgSeen",
    "animatedCgSeen"
]

MARKER = "__ADDED_BY_SCRIPT__"


def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_json(data, path):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def make_keys(text):
    text = " ".join(text.split())
    text = text.upper()

    return [
        text.replace(" ", "_"),
        text.replace(" ", "-")
    ]


def add_text(data, text):

    keys = make_keys(text)
    added = False

    for section in TARGET_SECTIONS:

        if section not in data:
            continue

        obj = data[section]

        if MARKER not in obj:
            obj[MARKER] = 1

        for key in keys:
            if key not in obj:
                obj[key] = 1
                added = True

    return added