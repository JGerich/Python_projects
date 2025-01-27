# Simple Password Generator in Python

#import the random and string modules to use them to generate random values:
import random
import string

#defining the function for the password generator:
def password_generator():
    #define the length of the password:
    length = 16
    
    #define the characters that the password will contain:
    #  string.ascii_letters: A string of all uppercase and lowercase English letters (i.e., "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ").
    #  string.digits: A string of all decimal digit characters (i.e., "0123456789").
    #  string.punctuation: A string of all common punctuation characters (e.g., !"#$%&'()*+,-./:;<=>?@[\\]^_{|}~`).
    
    characters = string.ascii_letters + string.digits + string.punctuation
    
    #generate a random password:
    password = ''.join(random.choice(characters) for i in range(length))
    
    #print the generated password:
    print("Your password is: ", password)
    
    return password

#start the script:
password_generator()


