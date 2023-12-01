import hashlib
from itertools import combinations, permutations

def combine_words(data):
    f1,f2=0,0
    cased_data = []
    for elem in data:
        cased_data.extend([elem.upper(),elem.title()])
    data.extend(cased_data)
    data = list(set(data))

    comb_list = [l for i in range(3) for l in combinations(data, i+1)]

    perm_list = []

    for elem in comb_list:
        perm_list += [''.join(p) for p in permutations(elem)]

    
    for elem in perm_list:
        h = hashlib.sha256((elem+salt).encode()).hexdigest()
        if h==hash_value and f1!=1:
            f1=1
            print("For first hash, found password: ", elem)
        if h==bonus_hash_value and f2!=1:
            f2=1
            print("For bonus hash, found password: ", elem)
        if f1==1 and f2==1:
            break
            
    if f1==0 and f2==0:
        print("Password not found")

personal_data = ['laplusbelle','marie','curie','woof','ukc','jean','neoskour','jvaist','fairecourir','eltrofor','80','81','1980','1981','123','@123','1234','@1234',
                 '02011980','29121981','020180','291281','01021980','12291981','010280','122981', 'january','december','29','2','02','1','01']

hash_value = '3281e6de7fa3c6fd6d6c8098347aeb06bd35b0f74b96f173c7b2d28135e14d45'
bonus_hash_value = 'fc2298f491eac4cff95e7568806e088a901c904cda7dd3221f551e5b89b3c3aa'
salt = '5UA@/Mw^%He]SBaU'

combine_words(personal_data)

