import hashlib
from itertools import combinations, permutations

x = 'abcdefghi'

hash_value = '91077079768edba10ac0c93b7108bc639d778d67'

comb_list = [''.join(l) for i in range(len(x)) for l in combinations(x, i+1)]
perm_list = []

for elem in comb_list:
    perm_list += [''.join(p) for p in permutations(elem)]

f=0
for word in perm_list:
    word_hash = hashlib.sha1((word).encode()).hexdigest()
    if word_hash == hash_value:
        f=1
        print("Passcode decoded to be : ", word)
        break

if f==0:
    print("Passcode not found")

"""OUTPUT: Passcode decoded to be :  aebfcidhg"""