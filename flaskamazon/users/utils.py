import random
import string

def get_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

def get_random_email(length):
    letters = string.ascii_lowercase
    upper = ''.join(random.choice(letters) for i in range(length))
    return upper+'@gmail.com'
