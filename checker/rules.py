
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
def check_numbers(password):
    for char in password:
        if char.isdigit():
            return True 
    return False

# check special characters 
def check_special_characters(password):
    special_characters = "!@#$%^&*()-_=+[]{}|\\:;\"'<>,.?/"

    for char in password:
        if char in special_characters:
            return True

    return False

# calculate score 
def calculate_score(length, uppercase, lowercase, numbers, special):
    score = 0

    if length:
        score += 1

    if uppercase:
        score += 1

    if lowercase:
        score += 1

    if numbers:
        score += 1

    if special:
        score += 1

    return score

def password_strength(score):
    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Medium"
    else:
        return "Strong"
    

def get_suggestions(length, uppercase, lowercase , numbers , special):
    suggestions=[]
    if length==False:
        suggestions.append("Password should be atleast of 8 characters")
    if not uppercase:
        suggestions.append("Password should have atleast one uppercase character")
    if not lowercase:
        suggestions.append("Password should have atleast one lowercase character")
    if not numbers:
        suggestions.append("Password should have a number")
    if not special:
        suggestions.append("Password do not have any special character")
    return suggestions 