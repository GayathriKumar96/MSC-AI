import random 
import string

def user_registration(u,p,pl):
    s = ''.join(random.choice(string.ascii_letters) for i in range(12))
    i=1
    h = hash(p+s)

    while i<=10:
        h = hash(h)
        i+=1

    print("Entering details into database....")
    with open("Assignment 2/user_info.txt", "a") as f:
        f.write("Username:-{0}||Salt:-{1}||Hash value:-{2}||Profile:-{3}\n".format(u,s,h,pl))
    
    print("Done!")

def user_login(u,p):
    print("Checking user from database....")
    with open("Assignment 2/user_info.txt", "r") as f:
        records = f.readlines()

    user_details = []
    for record in records:
        user_dict = {}
        details = record.split('||')
        for elem in details:
            category, value = elem.split(':-')
            user_dict[category] = value
        user_details.append(user_dict)
    print(user_details)    
        
    

choice = '1'

while choice in ['1','2']:

    choice = input("\n1. Register\n2. Login\nEnter the option: ")

    if choice == '1':
        u = input("Enter username: ")
        p = input("Enter password(clear): ")
        print("Enter profile information: ")
        name = input("Enter name: ")
        age = input("Enter age: ")
        gender = input("Enter gender: ")
        pl = {"name":name,"age":age,"gender":gender}
        user_registration(u,p,pl)

    elif choice=='2':
        print("Enter login details: ")
        u = input("Enter username: ")
        p = input("Enter password(clear): ")
        user_login(u,p)
    



