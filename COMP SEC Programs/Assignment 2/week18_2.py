from random import randint, random
import hashlib
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import base64

def generate_random_key():
    return hashlib.sha256((str(random())).encode())

def encrypt(plaintext, key):
    cipher = Cipher(algorithms.AES(key), modes.CFB(b'0000000000000000'), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(plaintext.encode())
    return base64.urlsafe_b64encode(ciphertext).decode()

def decrypt(ciphertext, key):
    cipher = Cipher(algorithms.AES(key), modes.CFB(b'0000000000000000'), backend=default_backend())
    decryptor = cipher.decryptor()
    plaintext = decryptor.update(base64.urlsafe_b64decode(ciphertext))
    return plaintext.decode()

k_as = generate_random_key()
k_bs = generate_random_key()
K_AS = k_as.digest()
K_BS = k_bs.digest()
k_as = k_as.hexdigest()
k_bs = k_bs.hexdigest()

print("\nPre-shared key between Alice and Server: ",k_as)
print("Pre-shared key between Bob and Server: ",k_bs)

n_a = randint(1000000000000000000,9999999999999999999)
print("\n1 (Alice): N_A = ",n_a)
print("1 (Alice => Server): (A, B, N_A)) = (Alice, Bob, {0})".format(n_a))

k_ab = generate_random_key()
K_AB = k_ab.digest()

k_ab = k_ab.hexdigest()
print("\n2 (Server): K_AB = ",k_ab)

E_kbs__kab_a = encrypt(k_ab+"||Alice",K_BS)
print("2 (Server): E_{{K_BS}} (K_AB, A) = E_{{{0}}} ({1}, Alice) = {2}".format(k_bs, k_ab,E_kbs__kab_a))

E_kas__na_b_kab_kbskaba = encrypt(str(n_a)+"||Bob||"+k_ab+"||"+E_kbs__kab_a,K_AS)
print("2 (Server => Alice): E_{{K_AS}} (N_A, B, K_AB, E_{{K_BS}} (K_AB, A)) = E_{{{0}}} ({1}, Bob, {2}, {3}) = {4}".format(k_as,n_a,k_ab,E_kbs__kab_a, E_kas__na_b_kab_kbskaba))

A_M2 = decrypt(E_kas__na_b_kab_kbskaba,K_AS).split("||")
print("2 (Alice): (N_A, B, K_AB, E_{{K_BS}} (K_AB, A)) = ({0}, Bob, {1}, {2})".format(A_M2[0],A_M2[2],A_M2[3]))

if A_M2[-1] == E_kbs__kab_a:
    print("=> Message 2 Authentication was successful!")

    print("\n3 (Alice => Bob): E_{{K_BS}} (K_AB, A) = E_{{{0}}} ({1}, Alice) = {2}".format(k_bs,k_ab,E_kbs__kab_a))

    B_M3 = decrypt(E_kbs__kab_a, K_BS).split("||")
    print("3 (Bob): (K_AB, A) = ({0}, Alice)".format(B_M3[0]))
    if B_M3[0] == k_ab:
        print("=> Message 3 Authentication was successful!")

        n_b = randint(1000000000000000000,9999999999999999999)
        print("\n4 (Bob): N_B = ",n_b)

        E_kab__nb = encrypt(str(n_b),K_AB)
        print("4 (Bob => Alice): E_{{K_AB}} (N_B) = E_{{{0}}} ({1}) = {2}".format(k_ab,str(n_b),E_kab__nb))

        A_M4 = decrypt(E_kab__nb,K_AB)
        print("4 (Alice): N_B = ",A_M4)
        if A_M4 == str(n_b):
            print("=> Message 4 Authentication was successful!")

            E_kab__nb_minus_1 = encrypt(str(n_b - 1), K_AB)
            print("\n5 (Alice => Bob): E_{{K_AB}} (N_B-1) = E_{{{0}}} ({1}) = {2}".format(k_ab,n_b-1,E_kab__nb_minus_1))

            B_M5 = decrypt(E_kab__nb_minus_1,K_AB)
            print("5 (Bob): N_B - 1 = ",B_M5)

            if B_M5 == str(n_b-1):
                print("=> Message 5 Authentication was successful!")
                print("\nThe key agreed between Alice and Bob: ",k_ab)
            else:
                print("=> Message 5 Authentication failed!")
        else:
            print("=> Message 4 Authentication failed!")
    else:
        print("=> Message 3 Authentication failed!")
else:
    print("=> Message 2 Authentication failed!")






