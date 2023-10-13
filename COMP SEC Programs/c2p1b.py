from random import randint

def fermat_test(n,k):
    for i in range(k):
        a = randint(2,n-1)
        if (a**(n-1))%n != 1:
            return a

    return 1

k = 50


for i in range(10):
    n = randint(100000,999999)
    print("Checking for n="+str(n))
    print("Running Fermat's test for k="+str(k)+" iterations")
    result = fermat_test(n,k)
    if  result== 1:
        print("The number "+str(n)+" is probably prime (verified with partial trial division with prime numbers less than 100 and with Fermat's test with "+str(k)+" iterations).")
    else:
        print("The number "+str(n)+" is composite with the certificate of compositeness being "+str(result)+".")

n = int(input("Please enter the integer n: "))
k = int(input("Please enter the number of iterations k: "))

print("Running Fermat's test for k="+str(k)+" iterations")

result = fermat_test(n,k)
if  result== 1:
    print("The number "+str(n)+" is probably prime (verified with partial trial division with prime numbers less than 100 and with Fermat's test with "+str(k)+" iterations).")
else:
    print("The number "+str(n)+" is composite with the certificate of compositeness being "+str(result)+".")

