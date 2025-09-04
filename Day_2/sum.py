
def sum_nat():
    i=1
    sum=0
    while i<=n:
        sum+=i
        i+=1
    return sum
n=int(input("enter a number"))
print(sum_nat())