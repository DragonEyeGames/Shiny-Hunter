import json
import os

FILENAME = "hunting_data.json"

SETTINGSNAME = "settings.json"
ADDRESSNAME = "address.json"

hunting_data = {
    "Registeel": 0
}

def save_data(data_to_save):
    #with open("hunting_data.json", "w") as file:
        #json.dump(data_to_save, file, indent=4)
    pass

def load_data(default_data):
    # Check if the file exists before trying to open it
    #if not os.path.exists(FILENAME):
     #   return default_data
        
    #with open(FILENAME, "r") as file:
    #    return json.load(file)
    return default_data

def save_address(data_to_save):
    data_to_save = {"saved_string": data_to_save}
    with open(ADDRESSNAME, "w") as file:
        json.dump(data_to_save, file, indent=4)

def load_address(default_data):
    # Check if the file exists before trying to open it
    if not os.path.exists(ADDRESSNAME):
        return default_data
        
    with open(ADDRESSNAME, "r") as file:
        loaded_data = json.load(file)
        return loaded_data["saved_string"]

def save_settings(shiny, non_shiny):
    data_to_save = {
        "shiny": shiny,
        "non_shiny": non_shiny
    }
    with open(SETTINGSNAME, "w") as file:
        json.dump(data_to_save, file, indent=4)

def load_settings():
    # Check if the file exists before trying to open it
    if not os.path.exists(SETTINGSNAME):
        return "", ""
        
    with open(SETTINGSNAME, "r") as file:
        loaded_data = json.load(file)
        return loaded_data["shiny"], loaded_data["non_shiny"]