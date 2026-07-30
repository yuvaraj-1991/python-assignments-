#Main file here we will import our functions and start application 

import json 

with open('servers.json', 'r') as file:
    servers = json.load(file)

while True: 

        print(''' 
            ==================================================
                    Server Configuration Manager            
            ==================================================   

            1. Display Servers
            2. Search Server
            3. Add Server
            4. Update Server
            5. Delete Server
            6. Exit

                ''')

        user_choice = int(input("Enter your Choice : "))        

        if user_choice == 1:
                display_servers(servers)
        elif user_choice == 2:
                search_servers(servers)    
        elif user_choice == 3:
                add_servers(servers)  
        elif user_choice == 4:
                update_servers(servers)  
        elif user_choice == 5:
                delete_servers(servers) 
        elif user_choice == 6:
                print("Exiting!! Have a Nice Day! ")                               


        