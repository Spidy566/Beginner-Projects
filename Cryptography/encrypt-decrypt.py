import random
import string

chars = list(string.ascii_letters + string.digits + string.punctuation + " ")
key = chars.copy()
random.shuffle(key)
def encrypt(message):
    encrypted = ""
    for char in message:
        encrypted += key[chars.index(char)]
    return encrypted
def decrypt(message):
    decrypted = ""
    for char in message:
        decrypted += chars[key.index(char)]
    return decrypted

message = input("Enter a message: ")
encrypted = encrypt(message)
decrypted = decrypt(encrypted)
print("Encrypted:", encrypted)
cipher = input("Enter the cipher: ")
print("Decrypted:", decrypted)

