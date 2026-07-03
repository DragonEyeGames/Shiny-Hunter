import tkinter as tk

class SwShScreen(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#4a4a4a")

        label = tk.Label(
            self,
            text="Select the pokemon you want to hunt:",
            font=("Arial", 24),
            bg="#4a4a4a"
        )
        label.pack(pady=20)