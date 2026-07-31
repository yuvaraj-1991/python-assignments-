import json 

with open('servers.json', 'r') as file:
    servers = json.load(file)

#adding count for report and displaying them at the end

critical = 0
warning = 0
healthy = 0

for server in servers:
   

    hostname = server['Hostname']
    cpu_usage = int(server['CPU Usage'])
    memory_usage = int(server['Memory Usage'])
    disk_usage = int(server['Disk Usage'])
    status = server['Status']


    if status != "Running": 
        critical = critical + 1
        # print(f"CRITICAL: {hostname} is not running ") 
    elif cpu_usage >= 90:  
        critical = critical + 1  
        # print(f"CRITICAL: {hostname} CPU Usage is high : {cpu_usage}")
    elif memory_usage >= 90:
        critical = critical + 1
        # print(f"CRITICAL: {hostname} Memory Usage is high : {memory_usage}")   
    elif disk_usage >= 90:
        critical = critical + 1
        # print(f"CRITICAL: {hostname} Disk Usage is high : {disk_usage}")     
    elif cpu_usage >= 70:
        warning = warning + 1
        # print(f"WARNING : {hostname} CPU usage is high : {cpu_usage}")
    elif memory_usage >= 80:
        warning = warning + 1
        # print(f"WARNING : {hostname} Memory usage is high : {memory_usage}")  
    elif disk_usage >= 75:
        warning = warning + 1
        # print(f"WARNING : {hostname} Disk usage is high : {disk_usage}")      
    else:
        healthy = healthy + 1
        # print(f"{hostname} is HEALTHY")


print("========== SERVER HEALTH REPORT ==========")
print(f"Healthy Servers  : {healthy}")    
print(f"Warning Servers  : {warning}")  
print(f"Critical Servers  : {critical}")  
print("==========================================")

       
