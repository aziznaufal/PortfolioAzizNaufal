from model import PasswordModel
from view import PasswordView
from controller import PasswordController
import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    model = PasswordModel()
    view = PasswordView(root)
    controller = PasswordController(model, view)
    root.mainloop()