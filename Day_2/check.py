def check(a):
    if a.isalpha():
        return "alphabet"
    elif a.isdigit():
        return "digit"
    elif a in ['@', '/', '%', '_']:
        return "special character"
    else:
        return "invalid"
a=input("enter a string").strip()
print(check(a))