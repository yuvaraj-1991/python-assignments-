#Here we will test on how to save the Employee details to json 
import json

employees = [
    {"EmployeeID": 1,
     "Name": "Junior"},
     {"EmployeeID": 2,
     "Name": "Senior"},
     {"EmployeeID": 3,
     "Name": "Leader"},
]


# print(json.dumps(x))

# print(dir(json))

# json.dump("data/dictionary/list - to be saved", "filename - where to be saved") it takes 2 arguments

# with open('employees.json', 'w') as empFile:
#     json.dump(employees,empFile, indent=4)

with open("employees.json", "r") as filedata:
    data = json.load(filedata)
    print(type(data))
    print(type(data[0]["Name"]))