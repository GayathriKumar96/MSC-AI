n = int(input("Enter the value of n:"))

if n<1 or n > 25:
    print("Invalid")

bin_list =[]

for i in range(2**n):
    bin_string=str(bin(i)).replace('b','')
    if len(bin_string) < n:
        bin_string = bin_string.zfill(n)
    else:
        bin_string = bin_string[len(bin_string)-n:]
    bin_list.append(bin_string)

print(bin_list)