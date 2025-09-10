def delete1(li,p):
    for i in li:
        if p in li:
            li.remove(p)
            
    return li

li=[3,4,5,6,7,8]
print(delete1(li,4))