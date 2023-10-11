def naive_exp(n,e):
    result = 1
    for i in range(e):
        result *= n
    return result

def rec_exp(n,e):
    if e==0:
        return 1
    elif e==1:
        return n
    elif e%2 == 0:
        return rec_exp(n,e//2) * rec_exp(n,e//2)
    else:
        return n * rec_exp(n,(e-1)//2) * rec_exp(n,(e-1)//2)

def non_rec_exp(n,e):
    result = 1
    x = n
    b = str(bin(e))
    while b:
        if b[-1] == '1':
            result *= x
        x *= x
        b = b[:-1]
    return result

n = int(input("Enter n: "))
e = int(input("Enter e: "))

print("Naive exponentiation result: "+str(naive_exp(n,e)))
print("Recursive exponentiation result: "+str(rec_exp(n,e)))
print("Non Recursive exponentiation result: "+str(non_rec_exp(n,e)))