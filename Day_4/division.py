def division(n,d):
    try:
        result=n/d
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    else:
        print(f"The result of {n} divided by {d} is {result}")



n=int(input("Enter the numerator: "))
d=int(input("Enter the denominator: "))
division(n,d)