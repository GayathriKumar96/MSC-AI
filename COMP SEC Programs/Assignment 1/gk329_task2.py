""" This program takes two integers a and b and calculates the GCD of a and b using Extended Eucledian Algorithm(EEA).
The function used:
EEA(a,b): takes integers a and b returns the values g,x,y from the representation: g = x*a + y*b
This function also prints the values at r,s and t at each step.
"""

def EEA(a,b):
    r1=a
    r=b
    s1=1
    s=0
    t1=0
    t=1

    print("({0}, {1}, {2})".format(r,s,t))

    while r!=0:
        q= r1//r
        r1,r = r,r1-(q*r)
        s1,s = s,s1-(q*s)
        t1,t = t,t1-(q*t)
        print("({0}, {1}, {2})".format(r,s,t))
    g=r1
    x=s1
    y=t1

    return g,x,y

a = int(input("Please enter a: "))
b = int(input("Please enter b: "))
if a<=0 or b<=0:
    print("Invalid!")
else:
    print("------------------------------------")
    print("The values of (r, s, t) in the steps of EEA are: ")
    g,x,y = EEA(a,b)
    print("------------------------------------")
    print("The values of (g, x, y) are: ({0}, {1}, {2})".format(g,x,y))
    print("------------------------------------")



