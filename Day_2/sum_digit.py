def sum_digit(n):
    sum=0
    i=0
    while(i<=n):
           
        r=n%10  
        sum=sum+r
        n=n//10
        i=i+1
    return sum
n=int(input())
print(sum_digit(n))