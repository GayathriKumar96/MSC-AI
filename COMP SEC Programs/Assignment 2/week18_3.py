from random import randint
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import base64
from binascii import unhexlify

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

k_ab = "4046d50b59721d71c877120cd1901939ddfbaa325157a4cae8eed4a44a973a13"
K_AB = unhexlify(k_ab)
M3 = "4046d50b59721d71c877120cd1901939ddfbaa325157a4cae8eed4a44a973a13"
k_bs = "290fe011433337546ec63c913e6a734b17ae2e5d37d3d5c7f1eb9151a0badd59"
K_BS = unhexlify(k_bs)

print("\nUnknown to Eve:")
print("Pre-shared key between Alice and Server: [does not matter / unused in the attack]")
print("Pre-shared key between Bob and Server: ", k_bs)

print("\nKnown to Eve (collected from a previous session between Alice and Bob):")
print("Pre-recorded K_AB: ",k_ab)
print("Pre-recorded Message 3 (Alice => Bob): ",M3)

print("\n3 (Eve => Bob): E_{{K_BS}} (K_AB, A) = E_{{{0}}} ({1}, Alice) = {2}".format(k_bs,k_ab,M3))
print("3 (Bob): (K_AB, A) = ({0}, Alice)".format(k_ab))
print("=> Eve successfully passed Message 3 authentication!")

n_b = randint(1000000000000000000,9999999999999999999)
print("\n4 (Bob): N_B = ",n_b)

E_kab__nb = encrypt(str(n_b),K_AB)
print("4 (Bob => Eve): E_{{K_AB}} (N_B) = E_{{{0}}} ({1}) = {2}".format(k_ab,str(n_b),E_kab__nb))

E_M4 = decrypt(E_kab__nb,K_AB)
print("4 (Eve): N_B = ",E_M4)
if E_M4 == str(n_b):
    print("=> Eve successfully decrypted Message 4 to get N_B!")

    E_kab__nb_minus_1 = encrypt(str(n_b - 1), K_AB)
    print("\n5 (Eve => Bob): E_{{K_AB}} (N_B-1) = E_{{{0}}} ({1}) = {2}".format(k_ab,n_b-1,E_kab__nb_minus_1))

    B_M5 = decrypt(E_kab__nb_minus_1,K_AB)
    print("5 (Bob): N_B - 1 = ",B_M5)

    if B_M5 == str(n_b-1):
        print("=> Eve successfully passed Message 5 authentication!")
        print("\nEve successfully launched a reply attack to reuse a previously recorded session key agreed betwwen Eve and Bob:\n",k_ab)
    else:
        print("=> Eve failed!")
else:
    print("=> Eve failed!")

