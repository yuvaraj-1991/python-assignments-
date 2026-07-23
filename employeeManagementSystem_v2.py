#Here is the latest code of Employee Management System

import json

#Here we are importing Employee data 

with open("employees.json", "r") as empData:
    employees = json.load(empData)
    #print(data)
#==============================================================================================================================#

#here we are checking for User Input or User Choice 

while True:
    
    print("="*50)
    print("Employee Management System")
    print("="*50)
    print('''

    1. Add Employee 
    2. Display Employees
    3. Search Employee 
    4. Update Employee
    5. Delete Employee
    6. Exit
    ''')

    userChoice = int(input(" Enter Your Choice : "))

    if userChoice == 1:
        # print("You have entered 1. Add Employee! ")
        while True:
            employee = {}

            employee['EmployeeID'] = int(input("Enter Employee ID : "))
            employee['Name'] = input("Enter the Employee Name : ")
            employee['Age'] = int(input("Enter the Employee Age : "))
            employee['Department'] = input("Enter the Employee Department : ")
            employee['Salary'] = int(input("Enter the Employee Salary : "))


            employees.append(employee) #here we are appending it to the main employees list 

            with open('employees.json', 'w') as empfile:
                json.dump(employees, empfile, indent=4)
            

            #Displaying the employees 
            # with open('employees.json', 'r') as empfile:
            #     employees = json.load(empfile)
            for emp in employees:
                for key,values in emp.items():
                    print("-"*50)
                    print(f"{key} {values}")

            choice = input("Do you want to add another Employee : (y/n) ").strip().lower()
            
            if choice != 'y':
                break
    elif userChoice == 2:
        print("You have entered 2. Display Employees! ")
    elif userChoice == 3:
        print("You have entered 3. Search Employee! ")  
    elif userChoice == 4:
        print("You have entered 4. Update Employee! ")  
    elif userChoice == 5:
        print("You have entered 5. Delete Employee! ")  
    elif userChoice == 6:  
        print("Exiting! Have a nice day :-) ")
        break
    else:
        print("Invalid Choice, Please Enter Again! ")   