def get_password():
    password = input("Enter password :")
    return password
def check_length(password):
    if len(password) >=8:
        return True
def check_special_characters(password):
    special_character ="@#$%^&*()_+-=?/"
    for character in special_character:
        if character in password:
            return True
    return False
def check_numbers(password):
    numbers="1234567890"
    for numbers in numbers:
        if numbers in password:
            return True
    return False
total =0
def display_stregth(length_ok,special_ok, number_ok,total):
    if length_ok:
        print("Length: ✅ (Pass)")
        total = total+1
    else:
        print("Length: ❌ (Fail - Less than 8 chars)")
    if special_ok:
        print("Special Character: ✅ (Pass)")
        total = total+1
    else:
        print("Special Character: ❌ (Fail - None found) ")
    if number_ok:
        print("Number: ✅(Pass)")
        total = total+1
    else:
        print("Number: ❌ (Fail - None found) ")
    if total == 3:
        print("Password Strength: STRONG ✅")
    elif total == 2:
        print("Password Strength: MEDIUM ⚠️")
    else:
        print("Password Strength: WEAK ❌")
    return
password=get_password()
length_ok = check_length(password)
special_ok = check_special_characters(password)
number_ok=check_numbers(password)
display_stregth(length_ok,special_ok,number_ok,total)