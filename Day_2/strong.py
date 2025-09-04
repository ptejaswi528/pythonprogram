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
def palindrome(n):
    flag=0
    o = n
    sum= 0
    while n > 0:
      
        l= n % 10
        
        
        sum= sum + dact(l)
        
       
        n = n // 10
    if o==sum:
        print("strong")
    else:
        print("not strong")
n=int(input())
palindrome(n)