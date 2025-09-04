def words(n):
    i=0
    while i<=n:
        n=n%10
        if n==1:
            return "one"
        elif n==2:
            return "two"
        elif n==3:
            c="three"
        elif n==4:
            c="four"
        elif n==5:
            c="five"
        elif n==6:
            c="six"
        elif n==7:
            c="seven"
        elif n==8:
            c="eight"
        elif n==9:
            c="nine"
        else:
            return "zero"
    i=i+1
n=int(input())
print(words(n))
    