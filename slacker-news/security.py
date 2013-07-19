import hashlib
import random
from pbkdf2 import pbkdf2_hex

def hash(s):
    f = haslib.sha512()
    f.update(s)
    return f.digest().encode('hex')

def random_salt(length):
    '''Generate a random hexadecimal salt of given length'''
    salt = random.sample("0123456789abcdef", length)
    return ''.join(salt)


def verify_key(password, salt, key, iterations=50000):
    derived_key = calculate_key(password, salt, iterations)
    if hash(derived_key) == hash(key):
        return True
    return False

def calculate_key(password, salt, iterations=50000):
    return pbkdf2_hex(password,
                      salt,
                      iterations,
                      keylen=128,
                      hashfunc=hashlib.sha512)
