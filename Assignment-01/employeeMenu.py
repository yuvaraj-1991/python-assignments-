#here we will build the Employee Menu

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
        print("You have entered 1. Add Employee! ")
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
    

