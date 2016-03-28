#Caesar Cipher implementation by Cameron Wilson

import sys

shift = 2


def main():
        #Take user input to encrypt or decrypt
        print "encrypt or decrypt?"
        option = raw_input("-->")


        while(True):

            if option == "encrypt":


                print "please enter a key"
                key = raw_input("-->")
                print "You put " + str(key)
                encryptedKey = encrypt(key)
                print "would you like to decrypt the key?"
                answer = raw_input("-->")

                if answer == "yes":
                    decrypt(encryptedKey)
                    break
                else:
                    print 'k bai'
                    print " i will leave you with a file for later"
                    file = open('myfile.dat', 'w+')
                    file.write(encryptedKey);
                    break
            elif option == "decrypt":

                print "please enter the file containing the encrypted key"
                filename = raw_input("")

                with open(filename, 'r') as myfile:
                    decryptThisKey = myfile.read().replace('\n', '')

                    decrypt(decryptThisKey)
                    break
            else:
                print "please enter encrypt or decrypt as a command"
                break

#Encrypt the given key by applying the shift to each character in the key string
def encrypt(key):

    cipherText = ""

    for letter in key:

        cipherCharNum = ((ord(letter) - 32 + shift) % (127 - 32) + 32) #ascii  of the shifted character
        cipherText += chr(cipherCharNum) #append shifted character to ciphertext


    print cipherText
    return cipherText


'''

 Decrypt an encrypted key by taking away the shift value from each character in the encryptedKey string

 Note: This function assumes that each chracter has been shifted by value corresponding to this
       implementation of Caesar cipher. It will not correctly decrypt a string with a different shifted
       applied to it
'''
def decrypt(encryptedKey):

    plaintext = ""

    for letter in encryptedKey:

        plainCharNum = ((ord(letter) - 32 - shift) % (127 - 32) + 32) #ascii value of plaintext character
        plaintext += chr(plainCharNum) #append plaintext character to original plaintext

    print plaintext

main()
