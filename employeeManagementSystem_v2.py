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
            

            
            # with open('employees.json', 'r') as empfile:
            #     employees = json.load(empfile)           

            choice = input("Do you want to add another Employee : (y/n) ").strip().lower()
            
            if choice != 'y':
                break
    elif userChoice == 2:
        #Displaying the employees 
        print("You have entered 2. Display Employees! Her is the List of Employees: ")
        for emp in employees:
            print("-"*50)
            for key,values in emp.items():                    
                print(f"{key} : {values}")
    elif userChoice == 3:
        #Employee Search 
        empSearch = int(input("You have entered 3. Search Employee! Please enter the Employee ID : \n"))
        for emp in employees:
            if empSearch == emp['EmployeeID']:
                print("-"*50)
                print("Employee ID found!")
                for keys, values in emp.items():                    
                    print(f"{keys}: {values}")
                break    
        else:
            print("Employee ID Not Found! Try again")        

    elif userChoice == 4:
        updateEmp = int(input("You have entered 4. Update Employee! Please enter the Employee ID: "))
        for emp in employees:
            if emp['EmployeeID'] == updateEmp:
                for keys,values in emp.items():
                    print(f"{keys} : {values}") 
                        
                print(''' 
                        What would you like to update? 
                        
                        1. Name
                        2. Age
                        3. Department
                        4. Salary

                        ''')      
                menuChoice = int(input("Enter your choice : "))  

                if menuChoice == 1:
                    updatedName = input("Enter the Name to update : ")
                    emp['Name'] = updatedName
                   
                elif menuChoice == 2:
                    updatedAge = int(input("Enter the Age to update : "))
                    emp['Age'] = updatedAge
                    
                elif menuChoice == 3:
                    updatedDep = input("Enter the Department to update : ")                       
                    emp['Department'] = updatedDep 
                    
                elif menuChoice == 4:
                    updatedSal = int(input("Enter the Salary to update : "))
                    emp['Salary'] = updatedSal
                    
                else:
                    print("Invalid choice ! ")    

                with open('employees.json', 'w') as fil:
                        json.dump(employees, fil, indent=4)

                print("Employee updated successfully!")    

                break
        else:
            print("Employee ID not found! ")

    elif userChoice == 5:
        print("You have entered 5. Delete Employee! ")  
    elif userChoice == 6:  
        print("Exiting! Have a nice day :-) ")
        break
    else:
        print("Invalid Choice, Please Enter Again! ")   