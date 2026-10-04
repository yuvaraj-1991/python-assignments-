#The DevOps team maintains deployment configuration in JSON.
#Here we will practice json The automation script must load a base configuration, validate that required 
# settings exist, load an override configuration, merge the overrides into the base configuration, and produce 
# the final configuration as JSON.


import json

with open("config.json", 'r') as file:
    config_data = json.load(file)

# print(type(config_data))   

#Mandatory config keys
required_keys = ["application", "deployment", "logging", "test"]

for key in required_keys:
    if key in config_data:
        print("found")
    elif key not in config_data:
        print(f"{key} : not found")

with open("overrides.json", "r") as over_file:
    override_data = json.load(over_file)

# print(type(override_data))

print(config_data['deployment']['replicas'])
print("="*50)
print(override_data)