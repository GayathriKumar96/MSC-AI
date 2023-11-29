import urllib.request as request
import hashlib

def hashing_n_times(data, n):
    for i in range(n):
        data = hashlib.sha256((str(data)).encode()).hexdigest()
    return data

url = "https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Leaked-Databases/phpbb.txt"

input = request.urlopen(url)

pswd = '3ddcd95d2bff8e97d3ad817f718ae207b98c7f2c84c5519f89cd15d7f8ee1c3b'

ps_dict = {}

f=0
for line in input:
    key = line.decode('utf-8').replace('\n','')
    ps_dict[key] = []
    for i in range(1,4):
        result = hashing_n_times(key, i)
        if result == pswd:
            f=1
            print("Found password : {0} hashed {1} times(s) using sha256".format(key,i))
            break

if f==0:
    print("Not found")

"""Output: Found password : legende hashed 1 times(s) using sha256"""
