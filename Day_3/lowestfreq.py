def lowestfreq(str):
    l={}
    for i in str:   
        if i in l:
            l[i]+=1
        else:
            l[i]=1
        
    min=1000
    char=''
    for i in l:
        if l[i]<min:
            min=l[i]
            char=i      
    print(f"{char} {min}")
str=input("enter a string")
lowestfreq(str)