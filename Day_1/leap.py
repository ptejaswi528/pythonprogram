def leap():
    if (a % 4 == 0 and a % 100 != 0) or (a % 400 == 0):
        return "leap"
    else:
        return "not a leap"
a=int(input("a:"))
print(leap())