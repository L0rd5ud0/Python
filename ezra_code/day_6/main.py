'''
A function called user_name that generates a username 
from the user email.
'''

def user_name(email):
    username = email.split('@')
    return username[0]

print(user_name('ben@gmail.com'))

