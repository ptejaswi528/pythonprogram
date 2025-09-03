n=int(input("enter number of consumers"))
for i in range(n):
    cn=int(input("cn:"))
    cname=input("cname:")
    pmr=int(input("pmr:"))
    lmr=int(input("lmr:"))
    tu=pmr-lmr
    print(f"{cn}\n{cname}\n{pmr}\n{lmr}\ntotal: {tu}\ncbill: {round(tu*3.80,2)}")
