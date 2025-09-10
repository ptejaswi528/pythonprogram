def duplicate(li):
    l2=[]
    for i in li:
        if i in l2:
             count+=1
        else:
            l2.append(i)
    return l2
li=[4,5,6,7,8,4,5]
print(duplicate(li))