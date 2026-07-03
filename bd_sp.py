import tkinter as tk

class BdSpScreen(tk.Frame):
    def __init__(self, parent, back_callback):
        super().__init__(parent, bg="#4a4a4a")

        self.turtwig= tk.PhotoImage(file="images/turtwig.png")
        self.chimchar= tk.PhotoImage(file="images/chimchar.png")
        self.piplup= tk.PhotoImage(file="images/piplup.png")
        self.uxie= tk.PhotoImage(file="images/uxie.png")
        self.mesprit= tk.PhotoImage(file="images/mesprit.png")
        self.azelf= tk.PhotoImage(file="images/azelf.png")
        self.dialga= tk.PhotoImage(file="images/dialga.png")
        self.palkia= tk.PhotoImage(file="images/palkia.png")
        self.giratina= tk.PhotoImage(file="images/giratina.png")
        self.regigigas= tk.PhotoImage(file="images/regigigas.png")
        self.heatran= tk.PhotoImage(file="images/heatran.png")
        self.regirock = tk.PhotoImage(file="images/regirock.png")
        self.regice = tk.PhotoImage(file="images/regice.png")
        self.registeel = tk.PhotoImage(file="images/registeel.png")
        self.raikou= tk.PhotoImage(file="images/raikou.png")
        self.entei= tk.PhotoImage(file="images/entei.png")
        self.suicune= tk.PhotoImage(file="images/suicune.png")
        self.articuno= tk.PhotoImage(file="images/articuno.png")
        self.zapdos= tk.PhotoImage(file="images/zapdos.png")
        self.moltres= tk.PhotoImage(file="images/moltres.png")
        self.ho-oh= tk.PhotoImage(file="images/ho-oh.png")
        self.lugia=tk.PhotoImage(file="images/lugia.png")
        self.latios=tk.PhotoImage(file="images/latios.png")
        self.latias=tk.PhotoImage(file="images/latias.png")
        self.groudon=tk.PhotoImage(file="images/groudon.png")
        self.kyogre=tk.PhotoImage(file="images/kyogre.png")
        self.rayquaza=tk.PhotoImage(file="images/rayquaza.png")
        self.mewtwo=tk.PhotoImage(file="images/mewtwo.png")

        #Game title
        label = tk.Label(
            self,
            text="Brilliant Diamon and Shining Pearl",
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
        self.create_pokemon_button(350, 150, self.turtwig, "Turtwig")
        self.create_pokemon_button(450, 150, self.chimchar, "Chimchar")
        self.create_pokemon_button(550, 150, self.piplup, "Piplup")
        self.create_pokemon_button(50, 250, self.uxie, "Uxie")
        self.create_pokemon_button(150, 250, self.mesprit, "Mesprit")
        self.create_pokemon_button(250, 250, self.azelf, "Azelf")
        self.create_pokemon_button(350, 250, self.dialga, "Dialga")
        self.create_pokemon_button(450, 250, self.palkia, "Palkia")
        self.create_pokemon_button(550, 250, self.giratina, "Giratina")
        self.create_pokemon_button(650, 250, self.regigigas, "Regigigas")
        self.create_pokemon_button(50, 350, self.heatran, "Heatran")
        self.create_pokemon_button(150, 350, self.raikou, "Raikou")
        self.create_pokemon_button(250, 350, self.entei, "Entei")
        self.create_pokemon_button(350, 350, self.suicune, "Suicune")
        self.create_pokemon_button(450, 350, self.articuno, "Articuno")
        self.create_pokemon_button(550, 350, self.zapdos, "Zapdos")
        self.create_pokemon_button(650, 350, self.moltres, "Moltres")
        self.create_pokemon_button(50, 450, self.ho-oh, "Ho-oh")
        self.create_pokemon_button(150, 450, self.lugia, "Lugia")
        self.create_pokemon_button(250, 450, self.latios, "Latios")
        self.create_pokemon_button(350, 450, self.latias, "Latias")
        self.create_pokemon_button(450, 450, self.groudon, "Groudon")
        self.create_pokemon_button(550, 450, self.kyogre, "Kyogre")
        self.create_pokemon_button(650, 450, self.rayquaza, "Rayquaza")
        self.create_pokemon_button(50, 550, self.mewtwo, "Mewtwo")

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