def unique(li):
    li1=[]
    for i in li:
        if i not in li1:
            li1.append(i)
    return li1
li=[2,3,4,5,5,6,7]
print(unique(li))
    
