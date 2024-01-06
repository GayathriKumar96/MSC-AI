code_dict = {'r':4,'w':2,'x':1,'-':0}

perm_str = input("Enter permission string: ")

if len(perm_str) != 9:
    print("Invalid string length!")
else:
    if set([perm_str[0],perm_str[3],perm_str[6]]) not in [{'r'},{'-'},{'r','-'}] \
    or set([perm_str[1],perm_str[4],perm_str[7]]) not in [{'w'},{'-'},{'w','-'}] \
    or set([perm_str[2],perm_str[5],perm_str[8]]) not in [{'x'},{'-'},{'x','-'}]:
        print("Invalid characters/format in string!")
    else:
        sum=0
        for i in range(0,7,3):
            multiplier = 10**((6-i)/3)
            value = 0
            for j in range(i,i+3):
                value += code_dict[perm_str[j]]
            sum+=value*multiplier
        print("Octal representation: ",int(sum))
