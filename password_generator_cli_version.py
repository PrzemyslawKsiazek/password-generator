# program password generator terminal version
# Author Przemysław Książek

import random
import string

LETTERS = string.ascii_letters
NUMBERS = string.digits
PUNCTUATION = string.punctuation


print("""
Welcome to the password generator.
Thanks to this program you will have a safe password, which will not be broken by the dictionary.
A secure password is one that consists of a minimum of 15 characters and contains upper and lower case letters, numbers and special characters.
""")

def get_password_length():
    """
    returns how many characters the password should consist of
    """
    password_length = input("How long do you want your password: ")
    if int(password_length) < 10:
        print("A secure password must be at least ten characters long. ")
        password_length = input("How long do you want your password: ")
    else:
        return int(password_length)

def password_generation(length=10):
    """
    this function generates a password
    """

    global random_password
    characters = f'{LETTERS}{NUMBERS}{PUNCTUATION}'
    characters = list(characters)
    random.shuffle(characters)

    random_password = random.choices(characters, k=length)
    random_password = ''.join(random_password)

    return random_password

new_password = password_generation(get_password_length())

print(f'Here is your password: {random_password}')
print('I recommend you to write it down somewhere because it will be difficult to remember it.')
print('Thank you for using the programs')