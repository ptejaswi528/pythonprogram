def add(k,v):
    if k in a:
        print("Key already exists. Use update to change the value.")
    else:
        a[k] = v
    return a
def remove(a,k):
    if k in a:
        del a[k]
    return a
def update(a,k,v):
    if k in a:
        a[k]=v
    return a
def search(a,k):
    if k in a.keys():
        return a[k]
    else:
        return None
def display(a):
    if a:
        for k, v in a.items():
            print(f"{k}: {v}")
    else:
        print("Dictionary is empty")
def count(a):
    return len(a)
def check_value(a, v):
    if v in a.values():
        print("Value exists in the dictionary")
    else:
        print("Value does not exist in the dictionary")
a={}
while True:
    print("1. Add\n2. Remove\n3. Update\n4. Search\n5. Display\n6. Count\n7. Check Value\n8. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        k = input("Enter key: ")
        v = input("Enter value: ")
        print(add(k, v))
    elif choice == 2:
        k = input("Enter key to remove: ")
        print(remove(a, k))
    elif choice == 3:
        k = input("Enter key to update: ")
        v = input("Enter new value: ")
        print(update(a, k, v))
    elif choice == 4:
        k = input("Enter key to search: ")
        print(search(a, k))
    elif choice == 5:
        display(a)
    elif choice == 6:
        print(count(a))
    elif choice == 7:
        v = input("Enter value to check: ")
        check_value(a, v)
    elif choice == 8:
        break
    else:
        print("Invalid choice")
