from collections import Counter
import json
import os


def load_data_from_json(filepath):
    if os.path.isfile(filepath):
        with open(filepath, "r", encoding="utf8") as json_file:
            return json.load(json_file)


def get_ordered_dict(_dict):
    return dict(Counter(_dict).most_common())


def print_dict(_dict):
    for item, count in _dict.items():
        print('{} - {}'.format(item, count))


if __name__ == '__main__':
    path = './sales_log.json'
    try:
        json_data = load_data_from_json(path)
        if json_data is None:
            exit("File not found")
    except ValueError:
        exit("That is not JSON-file")

    ordered_dict = get_ordered_dict(json_data)
    print_dict(ordered_dict)