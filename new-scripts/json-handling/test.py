#here we will test a nested dictionary merge without deleting or overriding other values 

#We need COPY module

import copy

import json

with open("config.json", 'r') as file:
    config_data = json.load(file)

with open("overrides.json", "r") as over_file:
    override_data = json.load(over_file)    

final_config = copy.deepcopy(config_data)

for key,value in override_data.items():
    if key in final_config:
        if isinstance(final_config[key], dict) and isinstance(value, dict):
            final_config[key].update(value)
        else:
            final_config[key] = value
    else:
        final_config[key] = value   

with open("final_config.json", "w") as fil:
    json.dump(final_config, fil, indent=4)             