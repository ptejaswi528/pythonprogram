def frequency(li):
    n=len(li)
    fc={}
    count=0
    for i in li:
        if i in fc:
            fc[i]+=1
        else:
            fc[i]=1
    return fc    
    
li=[2,3,4,5,6,7,4]
print(frequency(li))