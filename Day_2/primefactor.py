def prime(n):
    i=1
    count=0
    while i<=n:
        if n%i!=0:
            count+=1
        i=i+1
    if count<=2:
        return True
    else:
        return False
def factor():
    for i in range(1,n+1):
        if n%i==0:
            if prime(i):
                print(i)
            
n=int(input())
factor()