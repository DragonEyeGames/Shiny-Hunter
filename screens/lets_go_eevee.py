import tkinter as tk

class LgeScreen(tk.Frame):
    def __init__(self, parent, back_callback):
        super().__init__(parent, bg="#4a4a4a")



        #Game title
        label = tk.Label(
            self,
            text="Let's go Eevee and Pikachu",
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

        #Back button

        back_button = tk.Button(
            self,
            text="Back",
            font=("Arial", 20),
            command=back_callback
        )
        back_button.place(x=340, y=420, width=100, height=40)

    #Pokemon creation script
    def create_pokemon_button(self, x, y, image, name):
        button = tk.Button(
            self,
            image=image,
            bg="#8f8d8d",
            activebackground="#bfbfbf",
            borderwidth=0
        )
        button.place(x=x, y=y, width=74, height=74)

        label = tk.Label(
            self,
            text=name,
            font=("Arial", 10),
            fg="black",
            bg="white"
        )
        label.place(x=x+4, y=y + 54, width=66, height=16)

        return button, label