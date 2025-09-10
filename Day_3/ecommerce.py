def add(li,a):
    li.append(a)
    return li 
def remove(li,r):
    if r in li:
        li.remove(r)
    else:
        print("element is not there")
    return li 
def search(li,s):
    if s in li:
        print("available")
    else:
        print("not available")
def total(li):
    print("total number of products",len(li))
def sort1():
    li.sort()
    print("sort:",li)
def clear1():
    li.clear()
    print("cleared list:",li)
li=[]
while True:
    print("1.ADD")
    print("2.Remove")
    print("3.search")
    print("4,display")
    print("5.total")
    print("6.sort")
    print("7.clear")
    print("8.exit")
    choice=int(input("enter choice"))
    if choice==1:
        a=int(input("enter element to add"))
        print("element is added",add(li,a))
    elif choice==2:
        r=int(input("enter element to remove"))
        print("element is removed",remove(li,r))
    elif choice==3:
        s=int(input("enter element to search"))
        search(li,s)
    elif choice==4:
        print("elements in list",li)
    elif choice==5:
        print("total:",total(li))
    elif choice==6:
        sort1()
    elif choice==7:
        clear1()
    
    elif choice==8:
        exit()
    else:
        print("invalid")



