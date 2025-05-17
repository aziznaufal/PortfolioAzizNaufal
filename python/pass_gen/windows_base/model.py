import string
import random

class PasswordModel:
    def generate(self, length, use_upper, use_lower, use_digits, use_symbols):
        if not any([use_upper, use_lower, use_digits, use_symbols]):
            raise ValueError("At least one character type must be selected.")

        characters = ''
        if use_upper:
            characters += string.ascii_uppercase
        if use_lower:
            characters += string.ascii_lowercase
        if use_digits:
            characters += string.digits
        if use_symbols:
            characters += string.punctuation

        return ''.join(random.choice(characters) for _ in range(length))
