def length():
    count=0
    for i in str:
        count+=1
    return count
def compare(str,str1):
    if str<str1:
        print(f"{str} is greater")
    elif str1>str:
        print(f"{str1} is greater")
    else:
        print("strings are equal")
 

str=input("enter a string ")
str1=input("enter another string")
print(length())
print("comparing string",compare(str,str1))
print("concatenation of strings:",str+str1)