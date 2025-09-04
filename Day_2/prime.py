def prime():
    i=1
    count=0
    while i<=n:
        if n%i!=0:
            count+=1
        i=i+1
    if count<=2:
        return "prime"
    else:
        return "not a prime"
n=int(input())
print(prime())