import pyperclip

class PasswordController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.set_controller(self)

    def handle_generate(self):
        try:
            length_str = self.view.length_var.get()
            if not length_str.isdigit() or int(length_str) < 1:
                self.view.show_error("Invalid input", "Password length must be a positive number.")
                return

            password = self.model.generate(
                int(length_str),
                self.view.use_upper.get(),
                self.view.use_lower.get(),
                self.view.use_digits.get(),
                self.view.use_symbols.get()
            )
            self.view.show_password(password)
        except ValueError as e:
            self.view.show_warning("Warning", str(e))

    def handle_copy(self):
        password = self.view.password_var.get()
        if password:
            pyperclip.copy(password)
            self.view.show_info("Copied", "Password copied to clipboard.")
        else:
            self.view.show_warning("No password", "Generate a password first.")