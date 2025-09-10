def total():
    counta=0
    countd=0
    counts=0
    for i in str:
        if (i>='a' or i<='z') or (i>='A' or i<='Z'):
            counta+=1
        elif (i>=0 or i<=9):
            countd+=1
        else:
            counts+=1
    print(f"number of alphabets{counta}\n number of digits{countd}\n number of special characters{counts}")

str=input("enter a string ")
total()