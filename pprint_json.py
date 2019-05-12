import json


def load_data(filepath):
    with open(filepath, 'r') as file_handler:
        return json.load(file_handler)


def pretty_print_json(json_data):
    print(json.dumps(json_data, ensure_ascii=False, indent=4, sort_keys=True))


if __name__ == '__main__':
    # filepath = "/Users/dns/Desktop/yandex/4_json/input.json"
    filepath = input("Enter a path to file: ")
    json_data = load_data(filepath)
    pretty_print_json(json_data)

