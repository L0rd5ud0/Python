'''
A function called hide_password that takes no parameters.
The function takes an input (a password) from a user and returns a hidden password.
'''

def hide_password(password):
    count = len(password)
    print(f"Password is {count} characters long")
    password_redacted = ''
    for i in password:
        password_redacted += '*'
    
    return password_redacted

user_password = input('Enter your password: ').lower()

print(hide_password(user_password))