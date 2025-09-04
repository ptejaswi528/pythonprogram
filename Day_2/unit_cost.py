def unit_cost(x):
    if x>=1 and x<=50:
        return x*3.80
    elif x>=51 and x<=100:
        return 50*3.80+(x-50)*4.20
    elif x>100 and x<200:
        return 50*3.80+50*4.20+(x-100)*5.10
    elif x>200 and x<300:
        return 50*3.80+50*4.20+100*5.10+(x-200)*6.30
    else:
        return 50*3.80+50*4.20+100*5.10+100*6.30+(x-300)*7.50
n=int(input("enter number of consumers"))
for i in range(n):
    cn=int(input("cn:"))
    cname=input("cname:")
    pmr=int(input("pmr:"))
    lmr=int(input("lmr:"))
    tu=pmr-lmr
    print(f"{cn}\n{cname}\n{pmr}\n{lmr}\ntotal: {tu}\ncbill: {unit_cost(tu)}")

