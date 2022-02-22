from logging import setLoggerClass

from argon2 import PasswordHasher


def search4vowels(phrase:str)->set:
    '''Return any vowels found in a supplied word'''
    vowels = set ('aeiou')
    return vowels.intersection(set(phrase))

def search4letters(phrase:str, letters:str)->set:
    '''Return a set of the 'letters' found in a 'phrase' '''
    return set(letters).intersection(set(phrase))
