def StudentGrades():
    name=input("Enter your name: ")
    marks=int(input("Enter your marks: "))
    
    print("Your name: ",name)
    print("Your marks: ",marks)
    
    if marks>=85 and marks <=100:
        print("Grade: A")
    elif marks>=70:
        print("Grade: B")
    elif marks>=50:
        print("Grade: C")
    else:
        print("Fail")

StudentGrades()    
