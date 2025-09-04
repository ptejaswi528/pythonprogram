def dact(n):
    i=1
    fact=1
    while(i<=n):
        if n==0:
            return 0
        else:
            fact=fact*i
        i+=1
    return fact
n=int(input("enter a number"))
print(dact(n))