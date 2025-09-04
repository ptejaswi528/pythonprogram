def sum_first(n):
    i=0
    while(n):
      
        l=n%10
        n=n//10
        f=n
        i=i+1
    return f+l
n=int(input())
print(sum_first(n))
