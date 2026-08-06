#Here we can start with the code

#Printing all Docker images that have 0 vulnerabilities 
#Generate a report containing all Docker images that have one or more vulnerabilities.
#DEVOPS-4001

import json

def load_images():
    with open('docker_images.json', 'r') as file:
        docker_images = json.load(file)
        return docker_images

docker_images = load_images()

count = 0 

# for image in docker_images:
#     if image["Vulnerabilities"] >= 1:
#         count += 1
#         print("="*50)
#         for key,value in image.items():
#             print(f"{key} : {value}")

# print (f'''

#     ========== VULNERABILITY REPORT ==========

#     Matching Images : {count}

#     ==========================================
#     ''')

#DEVOPS-4002 
#The Platform Team needs to identify large production Docker images. 

# for image in docker_images:
#     if image["Environment"] == "Production" and image["SizeMB"] > 1000:
#         count += 1
#         print("="*50)
#         for key, value in image.items():
#             print(f"{key} : {value}")

# print(f"The Count is : {count}")            

#DEVOPS-4003

