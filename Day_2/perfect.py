def perfect(n):
    sum=0
    o = n
    i=1
    for i in range(1,n):
      
        
        if n%i==0:  
            sum= sum+i
        
       
       
    if o==sum:
        print("perfect")
    else:
        print("not perfect")
n=int(input())
perfect(n)