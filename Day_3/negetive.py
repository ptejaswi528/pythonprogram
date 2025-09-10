def negetive(li):
    n=len(li)
    for i in range(n):
        if i<0:
            return i
ele=map(int,input("enter negetive numbers").split())
li=[]
li.append(ele)
print(negetive(li))