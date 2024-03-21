import os
import json

def load_data(resource_path):
    """
    Load data from a JSON file located at the specified path.
    """
    try:
        with open(resource_path, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"Resource file '{resource_path}' not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error decoding JSON data from '{resource_path}'.")
        return None

# Example resource usage
if __name__ == "__main__":
    resource_path = "resources/data.json"
    data = load_data(resource_path)
    if data:
        print("Data loaded successfully:")
        print(data)
