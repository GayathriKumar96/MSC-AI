import hashlib
from itertools import combinations, permutations

key_code_dict = {'a':'0','b':'1','c':'2','d':'3','e':'4','f':'5','g':'6','h':'7','i':'8'}
x = 'abcdefghi'

hash_value = '91077079768edba10ac0c93b7108bc639d778d67'

comb_list = [''.join(l) for i in range(len(x)) for l in combinations(x, i+1)]
perm_list = []

for elem in comb_list:
    perm_list += [''.join(p) for p in permutations(elem)]

f=0
for word in perm_list:
    word_code = ''
    for letter in word:
        word_code += key_code_dict[letter]
    word_hash = hashlib.sha1((word_code).encode()).hexdigest()
    if word_hash == hash_value:
        f=1
        print("Passcode decoded to be : ", word)
        break

if f==0:
    print("Passcode not found")

"""OUTPUT: """