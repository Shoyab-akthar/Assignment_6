import json

file_path = 'assignment6-1\details.json' 

def read_json(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error decoding JSON in '{file_path}'. Please check the JSON format.")
        return None

def main():
    data = read_json(file_path)

    if data:
        print(json.dumps(data, indent=4))

if __name__ == "__main__":
    main()