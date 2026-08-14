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

# count = 0 

# for image in docker_images:
#     if (
#         image["Environment"] == "Production"
#         and image["Vulnerabilities"] > 0
#         and image["LastUpdatedDays"] > 90
#         ):
#         count += 1
#         print("="*50)
#         for key, value in image.items():
#             print(f"{key} : {value}")

# print("="*50)
# print(f"Risky production images are : {count}")
# print("="*50)

#DEVOPS-5001
#Incident: Disk usage is increasing rapidly on our Docker hosts.

# with open('docker-img.txt', 'r') as file:
#     next(file) # Skip the first line header 
#     for line in file:
#         row_data = line.strip().split(",")
#         print(row_data)

count = 0

docker_img_data = []

with open('docker-img.txt', 'r') as file:  
    next(file)
    all_lines = file.readlines()
    for line in all_lines:
        
        data = line.split() #converting into a list 
        size_row = data[-1] #extracting the last value 85MB or 1.2GB
        # print(size_row) 
        if size_row.endswith("MB"): #Using endswith keyword checking if MB/GB
            size_row = size_row[:-2] #String Slicing and removing MB 
            con_size_row = int(size_row) 
        elif size_row.endswith("GB"):
            size_row = size_row[:-2] #String Slicing and removing GB 
            con_size_row = float(size_row) * 1024 

        if con_size_row >= 1000:
            docker_img_data.append(con_size_row)
            docker_img_data.append(line)


print("================ Docker Images greater than 1000 =========================== ")
for img in docker_img_data:
    print(f"{img}")
print("================ Docker Images greater than 1000 =========================== ")            
  

   
