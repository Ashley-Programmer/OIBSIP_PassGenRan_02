import secrets
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation # Automatically include all character types

    if not characters:
        raise ValueError("No characters available for password generation.")

    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

def main():
    print("Random Password Generator")

    try:
        length = int(input("Enter desired password length(e.g. 12): "))
        if length <= 8:
            raise ValueError("Length must be more than 8 characters!")

        password = generate_password(length)
        print(f"\nYour generated password is:\n{password}")

    except ValueError as e:
        print(f"Error: {e}")

    print("\nThank you for using the Password Generator!")

if __name__ == "__main__":
    main()
