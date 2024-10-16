import string
import getpass

def check_password_strength(password):
    lower_alpha_count = upper_alpha_count = number_count = whitespace_count = special_char_count = 0
    for char in list(password):
        if char in string.ascii_lowercase:
            lower_alpha_count += 1
        elif char in string.ascii_uppercase:
            upper_alpha_count += 1
        elif char in string.digits:
            number_count += 1
        elif char == ' ':
            whitespace_count += 1
        else:
            special_char_count += 1
    strength = 0
    remarks = ''

    if lower_alpha_count >= 1:
        strength += 1
    if upper_alpha_count >= 1:
        strength += 1
    if number_count >= 1:
        strength += 1
    if whitespace_count >= 1:
        strength += 1
    if special_char_count >= 1:
        strength += 1

    if strength == 1:
        remarks = "This password is not secure. Change it as soon as possible."
    elif strength == 2:
        remarks = "That's not a good password. You should consider making it stronger."
    elif strength == 3:
        remarks = "Your password is okay, but it can be improved"
    elif strength == 4:
        remarks = "Your password is hard to guess. However you can make it more secure"
    elif strength == 5:
        remarks = "Well done that is a strong password. No further improvements are needed."

    print("Your password has:-")
    print(f"{lower_alpha_count} lowercase letters")
    print(f"{upper_alpha_count} uppercase letters")
    print(f"{number_count} digits")
    print(f'{whitespace_count} whitespaces')
    print(f"{special_char_count} special characters")
    print(f"Password score: {strength}/5")
    print(f"Remarks: {remarks}")

print("===== Welcome to Password Strength Checker =====")
while 1:
    choice = input("Do you want to check a password's strength (y/n) : ")
    if 'y' in choice.lower():
        password = getpass.getpass("Enter the password: ")
        check_password_strength(password)
    elif 'n' in choice.lower():
        print('Exiting...')
        break
    else:
        print('Invalid input...please try again.')
    
