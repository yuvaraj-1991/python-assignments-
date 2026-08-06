#Lets Start

import json

def load_servers():
    with open("servers.json", 'r') as file:
        servers = json.load(file)
        return servers

servers = load_servers()    

def display_servers(servers):    
    for server in servers:
        print("="*50)
        for key, value in server.items():
            print(f"{key} : {value}")

# display_servers(servers)

# while True:

#     print(''' 
            
#         1) Production
#         2) Development
#         3) QA
#         4) Staging
#         5) Exit
#             ''')

#     environment_input = int(input("Which Environment would you like to check : "))


#     if environment_input == 1:
#         for server in servers:
#            if server["Environment"] == "Production":                
#                 print("="*50)
#                 for key,value in server.items():
#                     print(f"{key} : {value}") 
#     elif environment_input == 2:
#         for server in servers:
#             if server["Environment"] == "Development":                
#                 print("="*50)
#                 for key,value in server.items():
#                     print(f"{key} : {value}") 
#     elif environment_input == 3:
#         for server in servers:
#             if server["Environment"] == "QA":                
#                 print("="*50)
#                 for key,value in server.items():
#                     print(f"{key} : {value}") 
#     elif environment_input == 4:
#         for server in servers:
#             if server["Environment"] == "Staging":                
#                 print("="*50)
#                 for key,value in server.items():
#                     print(f"{key} : {value}")                 
#     elif environment_input == 5:
#         break   


#Here we will have an loop to search for Ubuntu servers 

while True:

    print(''' 
            
        1) Ubuntu 22.04
        2) Rocky Linux 9
        3) Ubuntu 20.04
        4) Ubuntu 24.04
        5) Rocky Linux 8
        6) Exit
            ''')

    os_input = int(input("Which Operating System would you like to check : "))


    if os_input == 1:
        for server in servers:
           if server["OperatingSystem"] == "Ubuntu 22.04":                
                print("="*50)
                for key,value in server.items():
                    print(f"{key} : {value}") 
    elif os_input == 2:
        for server in servers:
            if server["OperatingSystem"] == "Rocky Linux 9":                
                print("="*50)
                for key,value in server.items():
                    print(f"{key} : {value}") 
    elif os_input == 3:
        for server in servers:
            if server["OperatingSystem"] == "Ubuntu 20.04":                
                print("="*50)
                for key,value in server.items():
                    print(f"{key} : {value}") 
    elif os_input == 4:
        for server in servers:
            if server["OperatingSystem"] == "Ubuntu 24.04":                
                print("="*50)
                for key,value in server.items():
                    print(f"{key} : {value}")     
    elif os_input == 5:
        for server in servers:
            if server["OperatingSystem"] == "Rocky Linux 8":                
                print("="*50)
                for key,value in server.items():
                    print(f"{key} : {value}")                              
    elif os_input == 6:
        break  