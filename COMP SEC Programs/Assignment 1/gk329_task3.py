""" This program takes an integer n and returns an n-bit prime
The functions used:
convert_to_bin(n): takes an integer n and returns its string binary form
exponentiation(m,e): takes integers m and e and returns result of (m^e).
approx_square_root(n): takes an integer n and returns the approximate square root of n
exhaustive_test(n): takes an integer n and tests it's primality using exhaustive trial approach
fermats_test(n): takes an integer n and tests it's primality using fermat's test for 50 iterations
check_prime(n): takes an integer n and performs exhaustive trial or fermat's test for primality depending on the value of n
find_n_bit_prime(n): takes an integer n and generates n-bit prime
"""



from random import randint

def convert_to_bin(n):
    b = ""
    if n==0:
        return "0"
    while n!=0:
        if n % 2 == 1:
            b+="1"
        else:
            b+="0"
        n//=2
    b = b[-1::-1]
    return b

def exponentiation(m,e):
    result = 1
    x = m
    b =convert_to_bin(e)
    while b:
        if b[-1] == '1':
            result *= x
        x *= x
        b = b[:-1]
    return result

def approx_square_root(n):
    i=1
    while i*i<=n:
        if i*i==n:
            return i
        i+=1
    return (i-1)

def exhaustive_test(n):
    for d in range(2,approx_square_root(n)+1):
        if n % d == 0:
            return 0
    return 1

def fermats_test(n):
    for i in range(50):
        a = randint(2,n-1)
        if (exponentiation(a,n-1))%n != 1:
            return 0
    return 1

def check_prime(n):
    if n<2:
        return 0
    if n<=541: #first 100 primes to use exhaustive approach
        if exhaustive_test(n) == 1:
            return 1
        return 0
    else:   #fermat's test for the rest of the numbers
        if fermats_test(n) == 1:
            return 1.1
        return 0

def find_n_bit_prime(n):
    if n<1:
        return -1,-1
    primes = []
    l = exponentiation(2,n-1)
    r = exponentiation(2,n)
    for i in range(l,r):
        prime_result = check_prime(i)
        if prime_result in [1,1.1]:
            primes.append([i, prime_result])
    if primes == []:
        return -1,-1
    return primes[randint(0,len(primes)-1)]

n = int(input("Please enter the parameter n: "))
p,i = find_n_bit_prime(n)
print("-----------------------------------------")
if p != -1:
    if i==1:
        print("The "+str(n)+"-bit prime is p = "+str(p))
    else:
        print("The "+str(n)+"-bit probably prime is p = "+str(p))
else:
    print("No primes found")
print("-----------------------------------------")