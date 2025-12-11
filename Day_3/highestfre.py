def highestfre():

    l={}
    for i in str:
        if i in l:
            l[i]+=1
        else:
            l[i]=1
    max=0
    char=''
    for i in l:
        if l[i]>max:
            max=l[i]
            char=i
    print(f"{char} {max}")

str=input("enter a string")
highestfre()
