from string import punctuation, ascii_uppercase, ascii_lowercase

def check_password_length(password):
    if len(password) < 8:
        return 'Password is too short'
    if len(password) > 64:
        return 'Password is too long'
    return True

def check_password_special(password):
    for char in password:
        if char in punctuation:
            return True
    return False

def check_password_uppercase(password):
    for char in password:
        if char in ascii_uppercase:
            return True
    return False

def check_password_lowercase(password):
    for char in password:
        if char in ascii_lowercase:
            return True
    return False

password = input('Your password: ')
requirements = {
    'length' : check_password_length(password),
    'lowercase' : check_password_lowercase(password),
    'uppercase' : check_password_uppercase(password),
    'special' : check_password_special(password)
}

for requirement in requirements:
    print(requirement, requirements[requirement])




    