# Random Password Generator

A simple, secure command-line password generator written in Python that creates cryptographically strong passwords using a variety of character types.

## Features

- **Cryptographically Secure**: Uses Python's `secrets` module for secure random generation
- **Comprehensive Character Set**: Includes uppercase letters, lowercase letters, digits, and punctuation marks
- **Customizable Length**: Generate passwords of any desired length
- **Error Handling**: Validates input and provides clear error messages
- **Simple Interface**: Easy-to-use command-line interface

## Requirements

- Python
- No external dependencies (uses only built-in Python modules)

## Installation

1. Clone or download the `main.py` file
2. Ensure you have Python installed on your system

## Usage

Run the script from your terminal or command prompt:

```bash
python main.py
```

The program will prompt you to enter your desired password length:

```
Random Password Generator
Enter desired password length(e.g. 12): 12

Your generated password is:
K#9mP@xL2$vN
```

## Character Set

The generator uses the following character types:
- **Uppercase letters**: A-Z (26 characters)
- **Lowercase letters**: a-z (26 characters)  
- **Digits**: 0-9 (10 characters)
- **Punctuation**: !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ (32 characters)

**Total**: 94 possible characters per position

## Security

This password generator uses Python's `secrets` module, which is designed for generating cryptographically strong random numbers suitable for managing secrets such as passwords, account authentication, security tokens, and related secrets.

### Password Strength
- 8 characters: ~52 bits of entropy
- 12 characters: ~78 bits of entropy
- 16 characters: ~105 bits of entropy

## Error Handling

The program handles common input errors:
- Non-numeric input for password length
- Negative or zero password length
- Invalid characters in length input

## Example Output

```
Random Password Generator
Enter desired password length(e.g. 12): 16

Your generated password is:
mK9#pL@x2$vN8qR!

Thank you for using the Password Generator!
```

## Security Best Practices

When using generated passwords:
1. Store passwords securely using a password manager
2. Use unique passwords for each account
3. Consider using longer passwords (12+ characters) for better security
4. Don't share passwords or store them in plain text

## License

This project is released into the public domain. Feel free to use, modify, and distribute as needed.

## Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.
