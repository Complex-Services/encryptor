import os
import sys

c = lambda: os.system('cls')

def encrypt(text):
    result = text.translate(encrypt_table)
    return result

def decrypt(message):
    result = message.translate(decrypt_table)
    return result

decrypted = b"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 "
encrypted = b"qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM)(*&^%$#@! "

encrypt_table = bytes.maketrans(decrypted, encrypted)
decrypt_table = bytes.maketrans(encrypted, decrypted)

while True:
    print("""[ Encryptor ]
          
[ 1 ] Encrypt
[ 2 ] Decrypt
[ x ] Exit""")
    text = input(": ")
    if text == '1':
        c()
        text = input('Encrypt: ')
        result = encrypt(text)
        print(f"{result}\n\nSave to file? (y/n)")
        save_result = input(": ")
        if save_result == 'y':
            c()
            f = open("encrypted.txt", "a+")
            f.write(f"{result}\n")
            f.close()
            print("[ Encryption saved ]")
            input("Enter to continue..")
            c()
            
        elif save_result == 'n':
            c()
            print("[ Encryption not saved ]")
            input("Enter to continue..")
            c()
            
        else:
            c()
            print("[ Invalid command ]")
            input("Enter to continue..")
            c()
        
    elif text == '2':
        c()
        cipherText = input('Decrypt: ')
        result = decrypt(cipherText)
        print(f"{result}\n\nSave to file? (y/n)")
        save_result = input(": ")
        if save_result == 'y':
            c()
            f = open("decrypted.txt", "a+")
            f.write(f"{result}\n")
            f.close()
            print("[ Decryption saved ]")
            input("Enter to continue..")
            c()
            
        elif save_result == 'n':
            c()
            print("[ Decryption not saved ]")
            input("Enter to continue..")
            c()
            
        else:
            c()
            print("[ Invalid command ]")
            input("Enter to continue..")
            c()
        
    elif text == 'x':
        sys.exit()
        
    else:
        c()
        print('Invalid command')
        input("Enter to continue.. ")
        c()
