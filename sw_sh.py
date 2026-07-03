import tkinter as tk

class SwShScreen(tk.Frame):
    def __init__(self, parent, back_callback):
        super().__init__(parent, bg="#4a4a4a")

        self.regirock = tk.PhotoImage(file="images/regirock.png")
        self.regice = tk.PhotoImage(file="images/regice.png")
        self.registeel = tk.PhotoImage(file="images/registeel.png")

        #Pokemon creation script
        def create_pokemon_button(self, x, y, image, name):
            button = tk.Button(
                self,
                image=image,
                bg="#8f8d8d",
                activebackground="#bfbfbf",
                borderwidth=0
            )
            button.place(x=x, y=y, width=70, height=70)

            label = tk.Label(
                self,
                text=name,
                font=("Arial", 10),
                fg="black",
                bg="white"
            )
            label.place(x=x, y=y + 50, width=70, height=20)

            return button, label

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

        self.create_pokemon_button(50, 150, self.regirock, "Regirock")
        self.create_pokemon_button(150, 150, self.regice, "Regice")
        self.create_pokemon_button(250, 150, self.registeel, "Registeel")

        #Back button

        back_button = tk.Button(
            self,
            text="Back",
            font=("Arial", 15),
            command=back_callback
        )
        back_button.place(x=370, y=440, width=60, height=25)