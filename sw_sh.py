import tkinter as tk
import config

class SwShScreen(tk.Frame):
    def __init__(self, parent, back_callback, boot_screen):
        super().__init__(parent, bg="#2b2b2b")

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
            text="Select a Pokémon to Hunt",
            font=("C052", 20),
            bg="#2b2b2b",
            fg="white"
        )
        label.pack(pady=20)

        self.border_box = tk.Frame(self, bg="black", width=702, height=202, relief="groove")
        self.border_box.pack_propagate(False)
        self.border_box.place(x = 49, y = 136)

        self.color_box = tk.Frame(self, bg="#5e5e5e", width=694, height=194, relief="groove")
        self.color_box.pack_propagate(False)
        self.color_box.place(x = 53, y = 140)

        self.create_pokemon_button(113, 150, self.regirock, "Regirock", boot_screen)
        self.create_pokemon_button(213, 150, self.regice, "Regice", boot_screen)
        self.create_pokemon_button(313, 150, self.registeel, "Registeel", boot_screen)
        self.create_pokemon_button(413, 150, self.regidrago, "Regidrago", boot_screen)
        self.create_pokemon_button(513, 150, self.regieleki, "Regieleki", boot_screen)
        self.create_pokemon_button(613, 150, self.virizon, "Virizion", boot_screen)
        self.create_pokemon_button(113, 150, self.terrakion, "Terrakion", boot_screen)
        self.create_pokemon_button(213, 250, self.cobalion, "Cobalion", boot_screen)
        self.create_pokemon_button(313, 250, self.arctovish, "Arctovish", boot_screen)
        self.create_pokemon_button(413, 250, self.arctozolt, "Arctozolt", boot_screen)
        self.create_pokemon_button(513, 250, self.dracovish, "Dracovish", boot_screen)
        self.create_pokemon_button(613, 250, self.dracozolt, "Dracozolt", boot_screen)

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

        label = tk.Label(
            self,
            text=name,
            font=("C052", 10),
            fg="black",
            bg="white"
        )
        label.place(x=x+4, y=y + 54, width=66, height=16)

        return button, label