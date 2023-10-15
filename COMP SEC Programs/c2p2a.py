from math import floor

a = int(input("Please enter the first integer: "))
b = int(input("Please enter the second integer: "))

if a<b:
    temp=a
    a=b
    b=temp

print("a = "+str(a)+",b = "+str(b)) 
print("Initialising:")
r1=a
r=b
s1=1
s=0
t1=0
t=1

print("r1 = "+str(r1)+", s1 = "+str(s1)+", t1 = "+str(t1)+"\nr = "+str(r)+", s = "+str(s)+", t = "+str(t)+"\n-------------------------------------------------------------------")

while r!=0:
    q=floor(r1/r)
    r1,r = r,r1-(q*r)
    s1,s = s,s1-(q*s)
    t1,t = t,t1-(q*t)

    print("q = "+str(q))
    print("r = "+str(q))
    print("s = "+str(q))
    print("t = "+str(q))
    print("r = s*a + t*b \n"+str(r)+" = "+str(s)+"*"+str(a)+" + "+str(t)+"*"+str(b))
    print("-------------------------------------------------------------------")

d=r1
x=s1
y=t1

print("The GCD of "+str(a)+" and "+str(b)+" is "+str(d))
print(str(d)+" = "+str(x)+"*"+str(a)+" + "+str(y)+"*"+str(b))