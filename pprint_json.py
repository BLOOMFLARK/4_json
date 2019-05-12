import json


def load_data(file_path):
    try:
        with open(file_path, 'r') as file_handler:
            return json.load(file_handler)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        return None


def pretty_print_json(json_data):
    print(json.dumps(json_data, ensure_ascii=False, indent=4, sort_keys=True))


if __name__ == '__main__':
    try:
        file_path = sys.argv[1]
        loaded_data = load_data(file_path)
        pretty_print_json(loaded_data)
    except FileNotFoundError:
        sys.exit('no files to load from')
