def vector_len_l2(b,m,n):
    vec_len = []
    for i in range(n):
        sum = 0
        for j in range(m):
            sum+=int(b[j][i])**2
        vec_len.append(sum)
    return vec_len

def inner_product(b,m,n):
    for i in range(n):
        for j in range(i+1,n):
            sum =0
            for l in range(m):
                sum+=int(b[l][i])*int(b[l][j])
            print("<b_{0}, b_{1}> = {2}".format(i+1,j+1,sum))
    return

filename = 'latt_n5_Mersene11.txt' 
#filename = 'latt_n5_Mersene19.txt'

b = []
with open(filename,'r') as f:
    data = f.readlines()
    for line in data:
        b.append(line.replace('\t\n','').split('\t'))

#inner_product(b,len(b),len(b[0]))