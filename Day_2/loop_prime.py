def prime(n):
    count=0
    i=1
    for i in range(i+1,n):
        for j in range(i,n):
            if i%j!=0:
                count+=1
        if count<=2:
            return i
n=int(input())
print(prime(n))
