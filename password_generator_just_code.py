import random
import string


def password_generator():
    
    length = 16    
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    
    print("Your password is: ", password)
    
    return password

password_generator()