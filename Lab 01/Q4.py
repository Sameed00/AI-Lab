def Calculator():
    
    while True:
        num=int(input("1. Add two numbers\n2. Subtract two numbers\n3. Exit\nEnter your choice: "))
        if num==3:
            break
        
        num1=int(input("Enter first number: "))
        num2=int(input("Enter second number: "))
        
        if(num==1):
            num3=num1+num2
        elif(num==2):
            num3=num1-num2
            
        else:
            print("Invalid input")
        
        print("Result: ",num3)
    
Calculator()    
