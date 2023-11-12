"""
This program takes the parameters N,e and c from task 4 and outputs the original message m 
that was encrypted to ciphertext c.
The functions used:
convert_to_bin(n): takes an integer n and returns its binary form
exponentiation(m,e): takes integers m and e and returns result of (m^e)
ind_cca(N,e,c): takes 3 parameters N,e and c and calculates the plaintext m
which was encrypted to ciphertext c
"""


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
    if e<0:
        return -1
    b =convert_to_bin(e)
    if b=='0':
        return 1
    while b:
        if b[-1] == '1':
            result *= x
        x *= x
        b = b[:-1]
    return result

def ind_cca(N,e,c):
    cp = (exponentiation(2,e)*c) % N
    print("The modified ciphertext c' is = ",cp)
    for i in range(N):
        if (2*i) % N == 1:
            inv =  i
            break
    print("The inverse of 2 mod {0} is = {1}".format(N, inv))
    print("--------------------------------------------------")
    print("Please decrypt the modified ciphertext c' using your program from Task 4.")
    mp = int(input("Please input the plaintext m' decrypted from c': "))
    m = int((inv*mp)%N)
    return m

try:
    N = int(input("Please enter the public parameter N: "))
    e = int(input("Please enter the encryption exponent e: "))
    print("--------------------------------------------------")
    c = int(input("Please enter the ciphertext c: "))
    print("--------------------------------------------------")
    if N<=0 or e<=0:
        raise Exception()
    m = ind_cca(N,e,c)
    print("The original plaintext message m computed from m' is: ",m)
    print("--------------------------------------------------")
except:
    print("INVALID!")
