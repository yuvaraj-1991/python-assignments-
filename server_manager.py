#Here we will start with Server Configuration 

import json 

# with open('servers.json', 'r') as file:
#     servers = json.load(file)


# print(servers_data)    

# for server in servers:    
#         print("-"*50)
#         for key,value in server.items():
#             print(f"{key} : {value}")


#Function to load servers

def load_servers():
     with open('servers.json', 'r') as file:
          servers = json.load(file)
          return servers

#Function to display servers     

def display_servers(servers):     
     for server in servers:
           print("-"*50)
           for key,value in server.items():
                 print(f"{key} : {value}")    

servers = load_servers()
display_servers(servers)

def search_servers(servers):
    findServer = int(input("Enter the Server ID : "))
    for server in servers:
        if server["ServerID"] == findServer:
            print("Server found! ")
            print("-"*50)
            for key, value in server.items():
                print(f"{key} : {value}")
            break
    else:
        print("Server not found!")          

          