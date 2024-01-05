import hmac
import hashlib

def generate_hmac(secret_key, msg):
    return hmac.new(secret_key.encode(), msg.encode(), hashlib.sha256).hexdigest()[:4]


secret_key = "NhqPtmdSJYdKjVHjA7PZj4Mge3R5YNiP1e3UZjInClVN65XAbvqqM6A7H5fATj0j"
message = "Alice, Bob, £10"
hmac_addr = generate_hmac(secret_key, message)
print("signature = ",hmac_addr)

fake_msg = "Alice, Eve, £1000"
fake_hmac = generate_hmac(secret_key, fake_msg)

if fake_hmac==hmac_addr:
    print("Server accepted the request")
else:
    print("Server rejected the request")

f=0
for amt in range(1,1000):
    fake_msg = "Alice, Bob, £"+str(amt)
    fake_hmac = hmac.new(secret_key.encode(), fake_msg.encode(), hashlib.sha256).hexdigest()[:4]

    if fake_hmac==hmac_addr:
        f=1
        print("Server accepted the request for amount £", amt)

if f==0:
    print("Server rejected request for amounts £1 till £1000")
