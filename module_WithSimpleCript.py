from simplecrypt import encrypt, decrypt

with open("encrypted.bin", mode="rb") as inp:
    encrypted = inp.read().strip()
    print(encrypted)
with open("passwords.txt", mode="r") as password:
    look = password.read().split()

for item in look:
    try:
        print(decrypt(item, encrypted))
    except:
        print("Error - {}".format(item))





