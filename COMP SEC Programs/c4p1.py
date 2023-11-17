def vector_len_l2(b,m,n):
    vec_len = []
    for i in range(n):
        sum = 0
        for j in range(m):
            sum+=int(b[j][i])**2
        vec_len.append(sum)
    return vec_len


#filename = 'latt_n5_Mersene11.txt' 
filename = 'latt_n5_Mersene19.txt'

b = []
with open(filename,'r') as f:
    data = f.readlines()
    for line in data:
        b.append(line.replace('\t\n','').split('\t'))

print(vector_len_l2(b,len(b),len(b[0])))




