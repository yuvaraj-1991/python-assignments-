#Here we will start with Server Configuration 



# with open('servers.json', 'r') as file:
#     servers = json.load(file)


# print(servers_data)    

# for server in servers:    
#         print("-"*50)
#         for key,value in server.items():
#             print(f"{key} : {value}")


import json 

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
    print("-"*50)
    print("-"*50)
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

search_servers(servers)            

def add_servers(servers):

    new_server = {}

    while True:

        server_id = int(input("Enter the New Server ID : "))

        for server in servers:
            if server['ServerID'] == server_id:
               print('Server ID already exists! Please enter again unique ID : ')
               break
        else:
            new_server['ServerID'] = server_id

                   
            host_name = input("Enter the HostName : ")
            new_server['Hostname'] = host_name

            ip_add = input("Enter the IP Address : ")
            new_server['IPAddress'] = ip_add

            environment = input("Enter the Environment QA/Dev/Prod : ")
            new_server['Environment'] = environment

            os_sys = input("Enter the Operating System : ")
            new_server['OperatingSystem'] = os_sys

            status = input("Enter the Status Run/Stopped/Paused : ")
            new_server['Status'] = status

            servers.append(new_server) #appending it to the list        

            print("Server Added Successfully! ")

            with open('servers.json','w') as fil:
                json.dump(servers,fil, indent=4)

            break     

        
add_servers(servers)             

