import random
import string

def generate_password(length, include_uppercase, include_lowercase, include_digits, include_special):
    # Initialize character sets based on user preferences
    character_pool = ''
    if include_uppercase:
        character_pool += string.ascii_uppercase
    if include_lowercase:
        character_pool += string.ascii_lowercase
    if include_digits:
        character_pool += string.digits
    if include_special:
        character_pool += string.punctuation

    if not character_pool:
        raise ValueError("At least one character type must be selected")

    # Ensure the password contains at least one of each selected type
    password = []
    if include_uppercase:
        password.append(random.choice(string.ascii_uppercase))
    if include_lowercase:
        password.append(random.choice(string.ascii_lowercase))
    if include_digits:
        password.append(random.choice(string.digits))
    if include_special:
        password.append(random.choice(string.punctuation))

    # Fill the remaining password length with random choices from the pool
    while len(password) < length:
        password.append(random.choice(character_pool))

    # Shuffle the password list to ensure randomness
    random.shuffle(password)

    return ''.join(password)

while True:
    try:
        # Gather user input for password preferences
        password_length = int(input("Enter the desired length for the password: "))
        include_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
        include_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
        include_digits = input("Include digits? (y/n): ").lower() == 'y'
        include_special = input("Include special characters? (y/n): ").lower() == 'y'
        
        # Generate the password
        generated_password = generate_password(password_length, include_uppercase, include_lowercase, include_digits, include_special)
        print("Generated Password:", generated_password)

    except ValueError as e:
        print(e)

    # Ask the user if they want to generate another password
    another = input("Do you want to generate another password? (y/n): ").lower()
    if another != 'y':
        break

print("Goodbye!")
