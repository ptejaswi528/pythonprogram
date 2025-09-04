def pass_fail(a):
    if a>40:
        if a>80 and a<100:
            return "S"
        elif a>70 and a<80:
            return "A"
        elif a>50 and a<70:
            return "B"
        else:
            return "pass"
    else:
        return "fail"

n=int(input("Enter number of students"))
for i in range(n):
    stn=int(input("Enter student number:"))
    stnm=input("Enter student name:")
    m1,m2,m3=map(int,input("enter maths,physics,chemistry marks").split())
    t=m1+m2+m3
    print(f"number: {stn}\nname: {stnm}\n marks: {m1,m2,m3}\ntotal: {t}\naverage: {t/3}\nGrade: {pass_fail(t)}")
    
         