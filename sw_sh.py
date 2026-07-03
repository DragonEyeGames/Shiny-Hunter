import tkinter as tk

class SwShScreen(tk.Frame):
    def __init__(self, parent, back_callback):
        super().__init__(parent, bg="#4a4a4a")

        self.regirock = tk.PhotoImage(file="images/regirock.png")


        #Game title
        label = tk.Label(
            self,
            text="Sword and Shield",
            font=("Arial", 30),
            bg="#4a4a4a"
        )
        label.pack(pady=20)

        #Text for the user to select a pokemon
        label = tk.Label(
            self,
            text="Select the pokemon you want to hunt:",
            font=("Arial", 24),
            bg="#4a4a4a"
        )
        label.place(x=70, y=80)

        regirock_button = tk.Button(
            self,
            image=self.regirock,
            bg="#bfbfbf",
            activebackground="#d0d0d0",
            borderwidth=2
        )
        regirock_button.place(x=50, y=150)
        back_button = tk.Button(
            self,
            text="Back",
            command=back_callback
        )
        back_button.place(x=625, y=680, width=30, height=30)