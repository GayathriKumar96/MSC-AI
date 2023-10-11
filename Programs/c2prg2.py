n = input("Enter the number:")

result = int(float(n))

if float(n)<0:
    result -= 1

print("Floor of "+ n + " is "+str(result))