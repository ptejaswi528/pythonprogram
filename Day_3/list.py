def list1(item):
    l=[]
    for i in item:
        if i not in l:
            l.append(i)
    return l
item=map(int, input("Enter numbers: ").split())
print(list1(item))