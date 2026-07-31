import json 

with open('servers.json', 'r') as file:
    servers = json.load(file)


for server in servers:
    hostname = server['Hostname']
    cpu_usage = int(server['CPU Usage'])
    memory_usage = int(server['Memory Usage'])
    disk_usage = int(server['Disk Usage'])
    status = server['Status']

    # print(hostname) 
    # print(cpu_usage) 
    # print(memory_usage)
    # print(disk_usage)
    # print(status)
    # print("-"*50)

    if status != "Running": 
        print(f"CRITICAL: {hostname} is not running ") 
    elif cpu_usage >= 90:    
        print(f"CRITICAL: {hostname} CPU Usage is high : {cpu_usage}")
    elif memory_usage >= 90:
        print(f"CRITICAL: {hostname} Memory Usage is high : {memory_usage}")   
    elif disk_usage >= 90:
        print(f"CRITICAL: {hostname} Disk Usage is high : {disk_usage}")     