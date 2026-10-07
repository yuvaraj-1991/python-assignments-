#Your team maintains Kubernetes deployment manifests. Before deployment, you need a Python utility that reads a manifest, 
# identifies the Deployment, and reports every container image it references.

# we will learn PyYAML  library using it we can parse yaml and can read the data in yaml files

import yaml

deploy_yaml_file = ('deployment.yaml')

with open(deploy_yaml_file, 'r') as file:
    deploy_yaml_data = yaml.safe_load(file)

# print(type(deploy_yaml_data))  
# print(type(deploy_yaml_data['spec']['template']['spec']['containers']))  

# print(f"The Deployment Name  {deploy_yaml_data ['kind'] } ")
print(f"The Deployment Name : {deploy_yaml_data['metadata']['name']}")
print(f"The Namespace : {deploy_yaml_data ['metadata']['namespace']}")
print(f"The Number of Replicas : {deploy_yaml_data ['spec']['replicas']}")


#We are storing the names of the container image here and then loop through each image-name
containers_list = deploy_yaml_data ['spec']['template']['spec']['containers']

print(containers_list)
# print(deploy_yaml_data['spec']['template']['spec']['containers'])

for container in containers_list:
    print(f"The Container Name : {container['name']}")
    print(f"The Container Image : {container['image']}")