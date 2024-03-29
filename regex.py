# regex.py

from re import *

pattern = compile('(^|\s)[-a-z0-9_.]+@([-a-z0-9]+\.)+[a-z]{2,6}(\s|$)')

def get_address():
    address = input('Enter your email address: ')
    is_valid = pattern.match(address)

    if is_valid:
        print('Valid Address:', is_valid.group())
    else:
        print('Invalid Address! Please Retry...\n')
        get_address()

get_address()

