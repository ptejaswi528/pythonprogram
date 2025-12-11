def count_occurances():
    li=list(str)
    fc={}
  
    for i in li:
        if i in fc:
            fc[i]+=1
        else:
            fc[i]=1
    for i in fc:
        print(f"{i}{fc[i]}",end="")

str=input("enter a string")
count_occurances()


