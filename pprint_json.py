import json
import sys


def load_data(file_path):
    try:
        with open(file_path, 'r') as file_handler:
            return json.load(file_handler)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        return None


def pretty_print_json(loaded_data):
    print(json.dumps(loaded_data, ensure_ascii=False, indent=4, sort_keys=True))


if __name__ == '__main__':

    if len(sys.argv) > 1:
        file_path = sys.argv[1]
    else:
        sys.exit('ERROR : no file path')

    loaded_data = load_data(file_path)
    if not loaded_data:
        sys.exit('ERROR : file not found or file not in a json format')
    else:
        pretty_print_json(loaded_data)
