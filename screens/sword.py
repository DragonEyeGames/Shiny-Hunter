import tkinter as tk
import config

class SwScreen(tk.Frame):
    def __init__(self, parent, back_callback, boot_screen):
        super().__init__(parent, bg="#2b2b2b")

        self.regirock = tk.PhotoImage(file="pokemon/regirock.png")
        self.regice = tk.PhotoImage(file="pokemon/regice.png")
        self.registeel = tk.PhotoImage(file="pokemon/registeel.png")
        self.regidrago = tk.PhotoImage(file="pokemon/regidrago.png")
        self.regieleki = tk.PhotoImage(file="pokemon/regieleki.png")
        self.virizon = tk.PhotoImage(file="pokemon/virizion.png")
        self.terrakion = tk.PhotoImage(file="pokemon/terrakion.png")
        self.cobalion = tk.PhotoImage(file="pokemon/cobalion.png")
        self.arctovish= tk.PhotoImage(file="pokemon/arctovish.png")
        self.arctozolt= tk.PhotoImage(file="pokemon/arctozolt.png")
        self.dracovish= tk.PhotoImage(file="pokemon/dracovish.png")
        self.dracozolt= tk.PhotoImage(file="pokemon/dracozolt.png")

        #Game title
        label = tk.Label(
            self,
            text="Sword and Shield",
            font=("Droid Sans Fallback", 35),
            bg="#2b2b2b",
            fg="white"
        )
        label.pack(pady=20)

        #Text for the user to select a pokemon
        label = tk.Label(
            self,
            text="Select a Pokemon to Hunt",
            font=("C052", 20),
            bg="#2b2b2b",
            fg="white"
        )
        label.pack()

        self.border_box = tk.Frame(self, bg="black", width=602, height=202, relief="groove")
        self.border_box.pack_propagate(False)
        self.border_box.place(x = 99, y = 166)

        self.color_box = tk.Frame(self, bg="#5e5e5e", width=594, height=194, relief="groove")
        self.color_box.pack_propagate(False)
        self.color_box.place(x = 103, y = 170)

        self.create_pokemon_button(113, 180, self.regirock, "Regirock", boot_screen)
        self.create_pokemon_button(213, 180, self.regice, "Regice", boot_screen)
        self.create_pokemon_button(313, 180, self.registeel, "Registeel", boot_screen)
        self.create_pokemon_button(413, 180, self.regidrago, "Regidrago", boot_screen)
        self.create_pokemon_button(513, 180, self.regieleki, "Regieleki", boot_screen)
        self.create_pokemon_button(613, 180, self.virizon, "Virizion", boot_screen)
        self.create_pokemon_button(113, 280, self.terrakion, "Terrakion", boot_screen)
        self.create_pokemon_button(213, 280, self.cobalion, "Cobalion", boot_screen)
        self.create_pokemon_button(313, 280, self.arctovish, "Arctovish", boot_screen)
        self.create_pokemon_button(413, 280, self.arctozolt, "Arctozolt", boot_screen)
        self.create_pokemon_button(513, 280, self.dracovish, "Dracovish", boot_screen)
        self.create_pokemon_button(613, 280, self.dracozolt, "Dracozolt", boot_screen)

        #Back button

        back_button = tk.Button(
            self,
            text="Back",
            font=("C052", 20),
            command=back_callback
        )
        back_button.place(x=340, y=420, width=100, height=40)

    #Initializes the hunt
    def start_hunt(self, pokemon_name, boot_screen):
        config.game_name="Sword and Shield"
        config.pokemon_name = pokemon_name
        boot_screen()

    #Pokemon creation script
    def create_pokemon_button(self, x, y, image, name, boot_screen):

        border_box = tk.Frame(self, bg="black", width=74, height=74, relief="groove")
        border_box.pack_propagate(False)
        border_box.place(x = x, y = y)

        button = tk.Button(
            self,
            image=image,
            bg="#8f8d8d",
            activebackground="#bfbfbf",
            command=lambda: self.start_hunt(name, boot_screen),
            borderwidth=0
        )
        button.place(x=x+2, y=y+2, width=70, height=70)

        border_box = tk.Frame(self, bg="black", width=66, height=16, relief="groove")
        border_box.pack_propagate(False)
        border_box.place(x = x+4, y = y+54)

        label = tk.Label(
            self,
            text=name,
            font=("C052", 9),
            fg="black",
            bg="white"
        )
        label.place(x=x+5, y=y + 55, width=64, height=14)

        return button, label