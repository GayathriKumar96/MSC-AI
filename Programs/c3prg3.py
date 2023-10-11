def euc(a,b):
    if b == 0:
        return a
    return euc(b,a%b)

a = int(input("Enter a: "))
b = int(input("Enter b: "))

print("GCD of "+str(a)+" and "+str(b)+ " is "+str(euc(a,b)))