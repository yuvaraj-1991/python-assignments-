#Here we are working on an issue Devops-5002 Title: Identify Unhealthy Docker Containers

# Write a Python program that:

# ✅ Reads the file.

# ✅ Skips the header.

# ✅ Identifies containers that are not healthy.

# Treat these as unhealthy:

# Exited
# Restarting
# Dead (if present)

# Ignore containers that are: Up ...

docker_unhealthy = []

with open('devops-5002.txt', 'r') as file:
    next(file)
    data = file.readlines()
    # print(data)
    for line in data:               
        if "Exited" in line:
            docker_unhealthy.append(line)            
        elif "Restarting" in line:
            docker_unhealthy.append(line)
        elif 'Dead' in line:
            docker_unhealthy.append(line)    
       
for img in docker_unhealthy:
    data = img.split()    
    # print(f"{data[1]} {data['Restarting']}{data[-1]}")
    print(f"Image : {data[1]}")
    if 'Restarting' in img:
        num = data.index('Restarting')
        str_data = data[num:-1]
        new_data = " ".join(str_data)
        print(new_data)
        print(f"Status : Restarting")
    elif 'Exited' in img:
        print(f"Status : Exited")
    elif 'Dead' in img:
        print(f"Status : Dead")    
    print(f"Container : {data[-1]}")
    print(f"{data[4:-1]}")
# print(docker_unhealthy)        

# ================ UNHEALTHY CONTAINERS ================

# Container : redis-db
# Image      : redis:7
# Status     : Exited (1) 3 hours ago

# ------------------------------------------------------

# Container : payment-api
# Image      : python:3.12
# Status     : Restarting (1) 10 seconds ago

# ======================================================