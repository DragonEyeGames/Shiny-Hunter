import json

hunting_data = {
    "Registeel": 0
}

def save_data(data_to_save):
    with open("hunting_data.json", "w") as file:
        json.dump(data_to_save, file, indent=4)