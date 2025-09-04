
def weekname(n):
        if(n==1):
              return "monday"
        elif(n==2):
               return "tuesday"
        elif n==3:
               return "wednesday"
        elif n==4:
               return "thursday"
        elif n==5:
               return "friday"
        elif n==6:
               return "saturday"
        elif n==7:
               return "sunday"
        else:
               return "invalid"
n=int(input("enter week name"))        
print(weekname(n))
