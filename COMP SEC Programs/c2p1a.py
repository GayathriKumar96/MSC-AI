from math import sqrt


def check_prime(n):
    limit = int(sqrt(n))

    if n>=2:
        if limit >=2:
            print("Searching for divisors between 2 and " + str(limit))
        else:
            print("Searching for divisors between 2 and 2")
    else:
        return -1,-1

    for i in range(2,limit+1):
        if n%i == 0:
            return 0,i  
    return 1,-1

n = int(input("Please enter the integer n: "))

f,i = check_prime(n)

if f==1:
    print("The number "+str(n)+" is a prime.")
elif f==0:
    print("The number "+str(n)+" is composite with the certificate of compositeness being "+str(i)+".")
else:
    print("Invalid!")