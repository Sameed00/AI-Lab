def EvenNumbers():
    num=int(input("Enter a number: "))
    
    count=0
    print("Even numbers: ")
    for x in range(1,num+1):
        if x%2==0:
            print (x)
            count+=1
    print("Total even numbers: ",count)
    
EvenNumbers()    
    
