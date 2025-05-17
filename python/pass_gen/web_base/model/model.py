import string
import random

class PasswordModel:
    def generate(self, length, use_upper, use_lower, use_digits, use_symbols):
        chars = ""
        if use_upper:
            chars += string.ascii_uppercase
        if use_lower:
            chars += string.ascii_lowercase
        if use_digits:
            chars += string.digits
        if use_symbols:
            chars += string.punctuation

        if not chars:
            raise ValueError("No character types selected")

        return ''.join(random.choice(chars) for _ in range(length))
