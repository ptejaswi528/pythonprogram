def armstrong(n):
    sum=0
    o = n
    r= 0
    while n > 0:
      
        l= n % 10
        
        
        sum= sum+(l**3)
        
       
        n = n // 10
    if o==sum:
        print("armstrong")
    else:
        print("not a armstrong")
n=int(input())
armstrong(n)