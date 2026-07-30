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

servers = load_servers()     

def find_servers(servers):
    for server in servers:
        print("-"*50)
        for key,value in server.items():
            print(f"{key} : {value}")
        return server    

#Function to display servers     

def display_servers(servers):     
     for server in servers:
           print("-"*50)
           for key,value in server.items():
                 print(f"{key} : {value}")    

servers = load_servers()
# display_servers(servers)

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

# search_servers(servers)            

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

        
# add_servers(servers)             

#Update Server 

def update_servers(servers):

    server_id_update = int(input("Enter Server ID to update : "))

    for server in servers:
        if server["ServerID"] == server_id_update:
            print("Current Server Configuration : ")
            print("-"*50)
            for key,value in server.items():
                print(f"{key} : {value}")
            # user_choice = int(input("Which field would you like to update : "))
            print (''' 
                    1. Hostname
                    2. IP Address
                    3. Environment
                    4. Operating System
                    5. Status
                    6. Exit
                        ''')
            while True:
                user_choice = int(input("Which field would you like to update : "))
                if user_choice == 1:
                    hostname = input("Enter the Hostname : ")
                    server["Hostname"] = hostname
                elif user_choice == 2:
                    ip_add = input("Enter the IP Address : ")  
                    server['IPAddress'] = ip_add
                elif user_choice == 3:
                    env = input("Enter Environment : ")
                    server["Environment"] = env               
                elif user_choice == 4:
                    operating_system = input("Enter Operating System : ")    
                    server["OperatingSystem"] = operating_system
                elif user_choice == 5:
                    status = input("Enter the current Status : ")
                    server["Status"] = status
                elif user_choice == 6:
                    print("Exiting!!")
                  

                    with open('servers.json', 'w') as fil:
                        json.dump(servers, fil, indent=4)
                        print("="*50)
                        print("Server updated successfully!")
                        print("="*50)
                        
                    break
            break
    else:
        print("Server ID not found!")    




# update_servers(servers)

def delete_servers(servers):

    server_id = int(input("Enter the Server ID : "))

    for server in servers:
        if server["ServerID"] == server_id:
            print("="*50)
            print("Server Found! ")
            print("="*50)
            for keys,values in server.items():
                print(f"{keys} : {values}")
            print("-"*50) 
            user_choice = input("Are you sure! you want to delete it? (Y/N)").strip().lower()
            if user_choice == "y":
                print("Deleting it!!!!!")
                servers.remove(server)
                print("Deleted Successfully! ")

                with open('servers.json', 'w') as fil:
                    json.dump(servers, fil, indent=4)
            else:
                print("Not Performing delete, Exiting")
            break
    else:
        print("Server ID not found! ")            


# delete_servers(servers)