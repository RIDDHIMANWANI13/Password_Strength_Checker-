# input password from user 
password = input("ENTER YOUR PASSWORD HERE :")

# to check the length of the password 
def check_length(password):
    if len(password)>=8:
        return True
    
    return False


# to check the password has uppercase character 
def check_uppercase(password):
    for char in password:
        if char.isupper():
            return True 
        
    return False 


# to check the password has lowercse character 
def check_lowercase(password):
    for char in password:
        if char.islower():
            return True
        
    return False 


# check numbers 
def check_number(password):
    for char in password:
        if char.isdigit():
            return True 
    return False


# main program 
length_result = check_length(password)
uppercase_result = check_uppercase(password)
lowercase_result = check_lowercase(password)
number_result = check_number(password)



print("\n----- PASSWORD REPORT -----")

if length_result:
    print("Password length is valid.")
else:
    print("Password must be at least 8 characters long.")

if uppercase_result:
    print("Contains uppercase letter.")
else:
    print("No uppercase letter found.")

if lowercase_result:
    print("Contains lowercase letter.")
else:
    print("No lowercase letter found.")

if number_result:
    print("Contains a number.")
else:
    print("No number found.")
