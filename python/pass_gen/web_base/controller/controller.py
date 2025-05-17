from model.model import PasswordModel

class PasswordController:
    def __init__(self):
        self.model = PasswordModel()

    def generate_password(self, length, use_upper, use_lower, use_digits, use_symbols):
        if not isinstance(length, int) or length < 1:
            raise ValueError("Password length must be positive integer.")
        if not any([use_upper, use_lower, use_digits, use_symbols]):
            raise ValueError("At least one character type must be selected.")
        return self.model.generate(length, use_upper, use_lower, use_digits, use_symbols)
