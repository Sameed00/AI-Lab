def calculate_average():
    num=int(input("Enter number of marks: "))
    
    Marks=[]
    for i in range(num):
        Marks.append(int(input("Enter marks: ")))
        
    total=0.0
    avg=0.0
    for i in range(num):
        total=total+Marks[i]
    
    avg=total/num
    print("Your Marks: ",Marks)
    print("Your average: ",avg)

calculate_average()    
        
    
