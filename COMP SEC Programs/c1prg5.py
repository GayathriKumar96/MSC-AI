def euc(a,b):
    if b == 0:
        return a
    return euc(b,a%b)


n = int(input("Enter n: "))

print("Z"+str(n),end = "\t\t")
for i in range(n):
    print(i,end="\t")
print()

for i in range(n):
    print(i,end = "\t\t")
    for j in range(n):
        print((i+j)%n,end="\t")
    print()

print("\n\n")

for i in range(n):
    for j in range(1,n+1):
        print(str(j)+"*"+ str(i)+ " mod " + str(n) + " = "+str((j*i)%n))


print("\n\n")

Znstar = [i for i in range(n) if euc(n,i) == 1]
print("Elements of Z"+str(n)+"* : "+str(Znstar))

print("\n\n")

for a in Znstar:
    for i in range(1,len(Znstar)+1):
        print(str(a)+"^"+ str(i)+ " mod " + str(n) + " = "+str((a**i)%n))

print("\n\n")


print("Z"+str(n)+"*",end = "\t\t")
for i in range(1,n):
    print(i,end="\t")
print()

for i in range(1,n):
    print(i,end = "\t\t")
    for j in range(1,n):
        print((i*j)%n,end="\t")
    print()
