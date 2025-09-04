def notes(n):
    count2=0
    while(n>0):
        if n>2000:
            n=n-2000
            count2=count2+1
        elif n>=500 and n<2000:
            n=n-500
            count2=count2+1
        elif n>=200 and n<500:
            n=n-200
            count2+=1
        elif n>=100 and n<200:
            n=n-100
            count2+=1
        elif n>=50 and n<100:
            n=n-50
            count2+=1
        elif n>=20 and n<50:
            n=n-20
            count2+=1
        elif n>=10 and n<20:
            n=n-10
            count2+=1
    return count2
n=int(input("enter amount"))
print(notes(n))
   
