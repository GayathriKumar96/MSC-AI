import hashlib

personal_data_prefix = ['laplusbelle','marie','curie','woof','ukc','jean','neoskour','jvaist','fairecourir','eltrofor']
personal_data_suffix = ['80','81','1980','1981','123','@123','1234','@1234']

hash_value = '3281e6de7fa3c6fd6d6c8098347aeb06bd35b0f74b96f173c7b2d28135e14d45'
salt = '5UA@/Mw^%He]SBaU '

f=0

for prefix in personal_data_prefix:
    for suffix in personal_data_suffix:
        h = hashlib.sha256((prefix+suffix+salt).encode()).hexdigest()
        if h==hash_value:
            f=1
            print("Found password: ", prefix+suffix)
            break

if f==0:
    print("Password not found")