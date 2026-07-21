#Lets Start

print("================= Employee Management ===================== ")



# print("Enter the employee details to add ")

# while True:
#     employee = {}

#     employee['EmployeeID'] = int(input("Enter Employee ID : "))
#     employee['Name'] = input("Enter the Employee Name : ")
#     employee['Age'] = int(input("Enter the Employee Age : "))
#     employee['Department'] = input("Enter the Employee Department : ")
#     employee['Salary'] = int(input("Enter the Employee Salary : "))

#     employees.append(employee) #here we are appending it to the main employees list 

#     choice = input("Do you want to add another Employee : (y/n) ").strip().lower()
    
#     if choice != 'y':
#         break

# #Here we are looping over each employee and displaying them using loops and all items from dictionary

# for emp in employees:
#     for key, value in emp.items():
#         print(f"{key} : {value}")
#     print("-" * 50)    

# #=================================================================================================================================

# #print(employees)

# #Search employee fucntionality 

# print("Enter the Employee ID to Search : ")

# employeeID = int(input("Enter the Employee ID to Search : "))

# # for employ in employees:
# #     for value in employ.items():
# #         if value == employeeID:
# #             print(employ)


# for employ in employees:
#     if employ['EmployeeID'] == employeeID:            
#         print(f"Employee found :  {employ}")        
#         break
# else:
#     print("No Employee found")    

#=================================================================================================================================
#Step 4: Input Validation





# if empID >= 1:
#     for emp in employees:
#         if empID == emp['EmployeeID']:
#             print("Employee ID already present!")                   
#             newEmpId = int(input("Enter unique Employee ID : "))
#             for emp in employees:
#                 if emp['EmployeeID'] == newEmpId:
#                     print("This is available")
#     else:
#         print("Employee ID is available, please enter the Employee name")       

# while True:

#     employee = {}

#     empID = int(input("Enter Employee ID : ")) 
#     for emp in employees: #Searching for duplicates 
#         if empID == emp['EmployeeID']:
#             print("Employee ID already present!")
#             break
#     else:
#         print("This is available")    #Now collecting the rest of the details after validating
#         employee['EmployeeID'] = empID             
#         employee['Name'] = input("Enter the Employee Name : ").strip().lower() 
#         while employee['Name'] == "":
#             print("Name cannot be empty string")
#             employee['Name'] = input("Enter the Employee Name : ") 
#         employee['Age'] = int(input("Enter the Employee Age : "))
#         employee['Department'] = input("Enter the Employee Department : ")
#         employee['Salary'] = int(input("Enter the Employee Salary : "))

#         employees.append(employee)

#         choice = input("Do you want to add another Employee : (y/n) ").strip().lower()

#         if choice != 'y':
#             break   
#     break

# while True:
#     employee = {}
    
#     employee['Name'] = input("Enter the Employee Name : ")
#     employee['Age'] = int(input("Enter the Employee Age : "))
#     employee['Department'] = input("Enter the Employee Department : ")
#     employee['Salary'] = int(input("Enter the Employee Salary : "))

#     employees.append(employee)

#     choice = input("Do you want to add another Employee : (y/n) ").strip().lower()

#     if choice != 'y':
#         break

#================================================================================================================================       
        # if empID != emp['EmployeeID']:
        #     print("This is available")
    # empID = int(input("Enter a unique Employee ID : "))
        
        # if empID != emp['EmployeeID']:
        #     print("This is available")
#================================================================================================================================

#Update an Employee

# empID = int(input("Enter the Employee ID to update : "))


# for employee in employees:
#     if empID == employee["EmployeeID"]:
#         print("Employee ID Found! ")
#         print("-" * 50)
#         for key, value in employee.items():
#             print(f"{key} {value}")
#         break
# else:
#     print(" Employee ID not found! ")
    
#================================================================================================================================

#You found the employee.  Now the system should ask:

# Employee Found!

# What would you like to update?

# 1. Name
# 2. Age
# 3. Department
# 4. Salary

# Enter your choice:

# print ("""
# Employee Found! 
# What would you like to update ?
# 1. Name 
# 2. Age 
# 3. Department
# 4. Salary
# """)

# menuChoice = int(input("Enter your Choice : "))


# if menuChoice == 1:
#     print("You selected Name ")
#     employee['Name'] = input("Enter the Employee Name : ")
#     print("Updated Successfully! ")
#     print("-"*50)
    

# elif menuChoice == 2:
#     print("You selected Age ")   
#     employee['Age'] = int(input("Update Age: "))
#     print("Updated Successfully! ")
#     print("-"*50)

# elif menuChoice == 3:
#     print("You selected Department ")
#     employee['Department'] = input("Enter Department: ")
#     print("Updated Successfully! ")
#     print("-"*50)

# elif menuChoice == 4:
#     print("You selected Salary ")    
#     employee['Salary'] = int(input("Enter Salary: "))
#     print("Updated Successfully! ")
#     print("-"*50)

# else:
#     print("Invalid choice")    

#================================================================================================================================
#Delete/Remove employee
# employee = {}

employees = [
    {"EmployeeID": 101, "EmployeeName": "Yuv"},
    {"EmployeeID": 102, "EmployeeName": "Sai"},
    {"EmployeeID": 103, "EmployeeName": "Dhruv"},
    {"EmployeeID": 104, "EmployeeName": "Abhi"},
    {"EmployeeID": 105, "EmployeeName": "Sam"}
    ]

delEmp = int(input("Enter the Employee ID to Delete : "))

for employee in employees:
    if employee["EmployeeID"] == delEmp:               
        print("Employee ID found! Deleting it...... ")
        employees.remove(employee)
        break    
else:
    print("Employee Not Found! ")    



