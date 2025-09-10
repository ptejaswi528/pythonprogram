def count1(li):
    counte=0
    counto=0
    n=len(li)
    for i in range(n):
        if li[i]%2==0:
            counte+=1
        else:
            counto+=1
    return counte,counto 

li =[2,3,4,5,6,7]

print(f"number of even and odd numbers{count1(li)}")