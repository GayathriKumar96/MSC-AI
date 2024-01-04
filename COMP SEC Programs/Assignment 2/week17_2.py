#should there be ui to upload password file?s

import random 
import string
import hashlib

def multiple_hashing(p_file,s):
    h = hashlib.sha256((p_file+s).encode()).hexdigest().strip()
    i=1
    while i<=10:
        h = hashlib.sha256((str(h)).encode()).hexdigest()
        i+=1
    return h

def user_registration(u,p):
    with open(".\\Assignment 2\\"+p, 'r') as file:
        p_file = file.read().strip()
    s = ''.join(random.choice(string.ascii_letters) for i in range(12))
    h = multiple_hashing(p_file,s)

    print("Entering details into database....")
    with open(".\\Assignment 2\\user_info_3.txt", "a") as f:
        f.write("Username:-{0}||Salt:-{1}||Hash value:-{2}\n".format(u,s,h))
    
    print("Done!")

def user_login(u,p):
    print("Checking user from database....")
    with open(".\\Assignment 2\\user_info_3.txt", "r") as f:
        records = f.readlines()

    user_details = []
    for record in records:
        user_dict = {}
        details = record.split('||')
        for elem in details:
            category, value = elem.split(':-')
            user_dict[category] = value
        user_details.append(user_dict)
    f=0
    for user in user_details:
        if user['Username'] == u:
            f=1
            s = user['Salt']
            with open(".\\Assignment 2\\"+p, 'r') as file:
                p_file = file.read().strip()
            h = multiple_hashing(p_file,s)
            hash_value = user['Hash value']
    if f==0:
        print("User not found!")           
    elif h.strip()==hash_value.strip():
        print("User logged in successfully!")
    else:
        print("Access denied!")

choice = '1'
while choice in ['1','2']:
    try:
        choice = input("\n1. Register\n2. Login\nEnter the option: ")

        if choice == '1':
            u = input("Enter username: ")
            p = input("Enter name of password file: ")
            user_registration(u,p)

        elif choice=='2':
            print("Enter login details: ")
            u = input("Enter username: ")
            p = input("Enter name of password file: ")
            user_login(u,p)
    except FileNotFoundError:
        print("Wrong file or file path")
