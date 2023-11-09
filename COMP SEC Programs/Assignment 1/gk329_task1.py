"""This program takes 3 parameters m,e and N to compute (m^e) modulo N. 
There are 2 functions defined. 
convert_to_bin(n): takes an integer n and returns its string binary form
exponentiation_modulo(m,e,N): takes integers m,e and N and returns string result of (m^e) modulo N. 

Exponentiation part done using non recursive binary logic.
Referred to the algorithm for the same given in: https://stackoverflow.com/questions/42598694/non-recursive-algorithm-of-ab-with-time-complexity-of-logb
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

def exponentiation_modulo(m,e,N):
    result = 1
    x = m
    if N<1:
        return -1
    if e<0:
        return -1
    b =convert_to_bin(e)
    if b=='0':
        return '1'
    while b:
        if b[-1] == '1':
            result *= x
        x *= x
        b = b[:-1]
    return str(result % N)

m = int(input("Please enter m: "))
e = int(input("Please enter e: "))
N = int(input("Please enter N: "))
print("-----------------------------------------------")
result = exponentiation_modulo(m,e,N)
if result == -1:
    print("Invalid!")
else:
    print("The value of m ∧ e mod N is: "+ result)
print("-----------------------------------------------")


