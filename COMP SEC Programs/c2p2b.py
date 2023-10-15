from math import floor

def mult_inv(n,a, Z_N_star):

    for i in Z_N_star:
        if (a*i)%n == 1:
            return i
    return -1

def EEA(a,b):
    if a<b:
        temp=a
        a=b
        b=temp
    r1=a
    r=b
    s1=1
    s=0
    t1=0
    t=1

    while r!=0:
        q=floor(r1/r)
        r1,r = r,r1-(q*r)
        s1,s = s,s1-(q*s)
        t1,t = t,t1-(q*t)

    d=r1
    x=s1
    y=t1

    return d,x,y

n = int(input("Please enter the integer N: "))

Z_N = []
Z_N_star = []

for i in range(1,n):
    d,x,y = EEA(n,i)
    Z_N.append((n,i,d,x,y))
    if d==1:
        Z_N_star.append(i)

for elem in Z_N:
    print("gcd("+str(elem[0])+","+str(elem[1])+") = "+str(elem[2])+" = "+str(elem[3])+"*"+str(elem[0])+" + "+str(elem[4])+"*"+str(elem[1]))
    if elem[2] == 1:
        inv = mult_inv(elem[0],elem[1],Z_N_star)
        if  inv != -1:
            print("(inverse of "+str(elem[1])+" = "+str(inv)+")")

print("(Z/"+str(n)+"Z)* = "+str(Z_N_star))