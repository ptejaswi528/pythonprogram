
n=int(input("Enter number of students"))
for i in range(n):
    stn=int(input("Enter student number:"))
    stnm=input("Enter student name:")
    m1,m2,m3=map(int,input("enter maths,physics,chemistry marks").split())

    print(f"number: {stn}\nname: {stnm}\n marks: {m1,m2,m3}\ntotal: {m1+m2+m3}\naverage: {(m1+m2+m3)/3}")
    
         


