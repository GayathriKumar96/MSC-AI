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

def check_prime(n):
    pass

def find_n_bit_prime(n):
    primes = []
    l = exponentiation(2,n-1)
    r = exponentiation(2,n)
    for i in range(l,r):
       if check_prime(i) == 1:
           primes.append(i)
    if primes == []:
        return -1
    return primes[randint(0,len(primes)-1)]