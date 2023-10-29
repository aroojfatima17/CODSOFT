import random
import string


def generatePassword(length, use_lowercase, use_uppercase, use_digits, use_special_chars):
    characters = ""

    if use_lowercase:
        characters += string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    if not characters:
        return "Requirement for generating password is insufficient \n Kindly regenerate with allowing characters"

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def get_requirements():
    print("Password Complexity Requirements:")
    print("TIP: Mark maximum yes to generate complex password")
    use_lowercase = input("Include lowercase letters? (y/n): ").lower() == "y"
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == "y"
    use_digits = input("Include digits? (y/n): ").lower() == "y"
    use_special_chars = input("Include special characters? (y/n): ").lower() == "y"

    return use_lowercase, use_uppercase, use_digits, use_special_chars


while True:
    try:
        length = int(input("What is your desired password length? (Enter digits)"))
        use_lowercase, use_uppercase, use_digits, use_special_chars = get_requirements()
        password = generatePassword(length, use_lowercase, use_uppercase, use_digits, use_special_chars)
        print("Generated Password:", password)
    except ValueError:
        print("Invalid input. Please enter a valid password length.")

    another = input("Do you want to generate another password? (y/n): ").lower()
    if another != "y":
        break
