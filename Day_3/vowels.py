def vowels():
    countv=0
    countc=0
    l=['a','e','i','o','u']
    for i in str:
        if i in l:
            countv+=1
        else:
            countc+=1
    return countv,countc 
str=input("enter a string ")
print(vowels())