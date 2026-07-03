import tkinter as tk

class LGScreen(tk.Frame):
    def __init__(self, parent, back_callback):
        super().__init__(parent, bg="#4a4a4a")

        label = tk.Label(
            self,
            text="Let's go Eevee and Pikachu",
            font=("Arial", 30),
            bg="#4a4a4a"
        )
        label.pack(pady=20)

        label = tk.Label(
            self,
            text="Select the pokemon you want to hunt:",
            font=("Arial", 24),
            bg="#4a4a4a"
        )
        label.pack(pady=20)

        back_button = tk.Button(
            self,
            text="Back",
            command=back_callback
        )
        back_button.pack()