import random
import string

def generate_password(length, complexity):
    if complexity == "low":
        characters = string.ascii_lowercase
    elif complexity == "medium":
        characters = string.ascii_letters + string.digits
    elif complexity == "high":
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        return "Invalid complexity level"
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Prompt the user for input
length = int(input("Enter the desired length of the password: "))
complexity = input("Enter the desired complexity level (low, medium, high): ")

# Generate the password
password = generate_password(length, complexity)

# Display the password
print(f"Generated Password: {password}")
