from checker.rules import (
    check_length,
    check_uppercase,
    check_lowercase,
    check_numbers,          
    check_special_characters,
    calculate_score,
    password_strength,
    get_suggestions,
    generate_password
)

# Input password from user
password = input("ENTER YOUR PASSWORD HERE: ")

# Check password rules
length_result = check_length(password)
uppercase_result = check_uppercase(password)
lowercase_result = check_lowercase(password)
number_result = check_numbers(password)   
special_result = check_special_characters(password)

# Calculate score
score = calculate_score(
    length_result,
    uppercase_result,
    lowercase_result,
    number_result,
    special_result
)

# Check strength
strength = password_strength(score)

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

if special_result:
    print("Contains a special character.")
else:
    print("No special character found.")

print("\nPassword Analysis")

print(f"Length (8+): {length_result}")
print(f"Uppercase: {uppercase_result}")
print(f"Lowercase: {lowercase_result}")
print(f"Numbers: {number_result}")
print(f"Special Characters: {special_result}")

print(f"\nPassword Score: {score}/5")
print(f"Password Strength: {strength}")

# Suggestions
suggestions = get_suggestions(
    length_result,
    uppercase_result,
    lowercase_result,
    number_result,
    special_result
)

print("\nSuggestions:")

if not suggestions:
    print("Excellent password! No suggestions needed.")
else:
    for suggestion in suggestions:
        print(f"- {suggestion}")

help=input("Do you want to generate a password (Y/N)")
if help=='Y':
    generated_password = generate_password()
    print(f"\nGenerated Password: {generated_password}")
 