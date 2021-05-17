from json import dump, load

def populate_json(filepath: str, data: list):
    with open(filepath, 'w') as file:
        dump(data, file, indent=2)

def get_json_data(filepath: str) -> list:
    with open(filepath, 'r') as file:
        return load(file)