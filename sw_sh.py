import tkinter as tk
import config

class SwShScreen(tk.Frame):
    def __init__(self, parent, back_callback, boot_screen):
        super().__init__(parent, bg="#4a4a4a")

        self.regirock = tk.PhotoImage(file="images/regirock.png")
        self.regice = tk.PhotoImage(file="images/regice.png")
        self.registeel = tk.PhotoImage(file="images/registeel.png")
        self.regidrago = tk.PhotoImage(file="images/regidrago.png")
        self.regieleki = tk.PhotoImage(file="images/regieleki.png")
        self.virizon = tk.PhotoImage(file="images/virizion.png")
        self.terrakion = tk.PhotoImage(file="images/terrakion.png")
        self.cobalion = tk.PhotoImage(file="images/cobalion.png")
        self.arctovish= tk.PhotoImage(file="images/arctovish.png")
        self.arctozolt= tk.PhotoImage(file="images/arctozolt.png")
        self.dracovish= tk.PhotoImage(file="images/dracovish.png")
        self.dracozolt= tk.PhotoImage(file="images/dracozolt.png")

        config.pokemon_name="Sword and Shield"

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

        self.create_pokemon_button(63, 150, self.regirock, "Regirock", boot_screen)
        self.create_pokemon_button(163, 150, self.regice, "Regice", boot_screen)
        self.create_pokemon_button(263, 150, self.registeel, "Registeel", boot_screen)
        self.create_pokemon_button(363, 150, self.regidrago, "Regidrago", boot_screen)
        self.create_pokemon_button(463, 150, self.regieleki, "Regieleki", boot_screen)
        self.create_pokemon_button(563, 150, self.virizon, "Virizion", boot_screen)
        self.create_pokemon_button(663, 150, self.terrakion, "Terrakion", boot_screen)
        self.create_pokemon_button(63, 250, self.cobalion, "Cobalion", boot_screen)
        self.create_pokemon_button(163, 250, self.arctovish, "Arctovish", boot_screen)
        self.create_pokemon_button(263, 250, self.arctozolt, "Arctozolt", boot_screen)
        self.create_pokemon_button(363, 250, self.dracovish, "Dracovish", boot_screen)
        self.create_pokemon_button(463, 250, self.dracozolt, "Dracozolt", boot_screen)

        #Back button

        back_button = tk.Button(
            self,
            text="Back",
            font=("Arial", 20),
            command=back_callback
        )
        back_button.place(x=340, y=420, width=100, height=40)

    #Pokemon creation script
    def create_pokemon_button(self, x, y, image, name, boot_screen):
        button = tk.Button(
            self,
            image=image,
            bg="#8f8d8d",
            activebackground="#bfbfbf",
            command=boot_screen,
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