def palindrome(n):
    flag=0
    o = n
    r= 0
    while n > 0:
      
        l= n % 10
        
        
        r= (r * 10) + l
        
       
        n = n // 10
    if o==r:
        print("palindrome")
    else:
        print("not a palindrome")
n=int(input())
palindrome(n)