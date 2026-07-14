import customtkinter as ctk
from PIL import Image

import config


class BdScreen(ctk.CTkFrame):

    def __init__(self, parent, back_callback, boot_screen):
        super().__init__( parent, fg_color="#050c15" )

        # Images
        self.dialga = ctk.CTkImage(light_image=Image.open("pokemon/dialga.png"),dark_image=Image.open("pokemon/dialga.png"),size=(70,70))
        self.giratina = ctk.CTkImage(light_image=Image.open("pokemon/giratina.png"),dark_image=Image.open("pokemon/giratina.png"),size=(70,70))
        self.arceus = ctk.CTkImage(light_image=Image.open("pokemon/arceus.png"),dark_image=Image.open("pokemon/arceus.png"),size=(70,70))
        self.azelf = ctk.CTkImage(light_image=Image.open("pokemon/azelf.png"),dark_image=Image.open("pokemon/azelf.png"),size=(70,70))
        self.heatran = ctk.CTkImage(light_image=Image.open("pokemon/heatran.png"),dark_image=Image.open("pokemon/heatran.png"),size=(70,70))
        self.uxie = ctk.CTkImage(light_image=Image.open("pokemon/uxie.png"),dark_image=Image.open("pokemon/uxie.png"),size=(70,70))
        self.mesprit = ctk.CTkImage(light_image=Image.open("pokemon/mesprit.png"),dark_image=Image.open("pokemon/mesprit.png"),size=(70,70))
        self.regigigas = ctk.CTkImage(light_image=Image.open("pokemon/regigigas.png"),dark_image=Image.open("pokemon/regigigas.png"),size=(70,70))
        self.regirock = ctk.CTkImage(light_image=Image.open("pokemon/regirock.png"),dark_image=Image.open("pokemon/regirock.png"),size=(70,70))
        self.regice = ctk.CTkImage(light_image=Image.open("pokemon/regice.png"),dark_image=Image.open("pokemon/regice.png"),size=(70,70))
        self.registeel = ctk.CTkImage(light_image=Image.open("pokemon/registeel.png"),dark_image=Image.open("pokemon/registeel.png"),size=(70,70))
        self.raikou = ctk.CTkImage(light_image=Image.open("pokemon/raikou.png"),dark_image=Image.open("pokemon/raikou.png"),size=(70,70))
        self.entei = ctk.CTkImage(light_image=Image.open("pokemon/entei.png"),dark_image=Image.open("pokemon/entei.png"),size=(70,70))
        self.suicune = ctk.CTkImage(light_image=Image.open("pokemon/suicune.png"),dark_image=Image.open("pokemon/suicune.png"),size=(70,70))
        self.latias = ctk.CTkImage(light_image=Image.open("pokemon/latias.png"),dark_image=Image.open("pokemon/latias.png"),size=(70,70))
        self.latios = ctk.CTkImage(light_image=Image.open("pokemon/latios.png"),dark_image=Image.open("pokemon/latios.png"),size=(70,70))
        self.ho_oh = ctk.CTkImage(light_image=Image.open("pokemon/ho-oh.png"),dark_image=Image.open("pokemon/ho-oh.png"),size=(70,70))
        self.kyogre = ctk.CTkImage(light_image=Image.open("pokemon/kyogre.png"),dark_image=Image.open("pokemon/kyogre.png"),size=(70,70))
        self.groudon = ctk.CTkImage(light_image=Image.open("pokemon/groudon.png"),dark_image=Image.open("pokemon/groudon.png"),size=(70,70))
        self.rayquaza = ctk.CTkImage(light_image=Image.open("pokemon/rayquaza.png"),dark_image=Image.open("pokemon/rayquaza.png"),size=(70,70))
        self.mewtwo = ctk.CTkImage(light_image=Image.open("pokemon/mewtwo.png"),dark_image=Image.open("pokemon/mewtwo.png"),size=(70,70))

        # Title
        title = ctk.CTkLabel(self,text="Pokemon Brilliant Diamond",font=("Arial", 35, "bold"),text_color="#2b89d9")

        title.pack(pady=(25, 10))


        # Subtitle
        label = ctk.CTkLabel(self,text="Select a Pokemon to Hunt",font=("Arial", 20),text_color="white")

        label.pack()


        # Outline box
        self.color_box = ctk.CTkFrame(self,fg_color="#21344a",width=594,height=194,corner_radius=15, border_width=5, border_color="black")

        self.color_box.place(x=103,y=170)


        # Pokemon buttons
        self.create_pokemon_button(50,135,self.dialga,"Dialga",boot_screen, True)
        self.create_pokemon_button(150,135,self.uxie,"Uxie",boot_screen)
        self.create_pokemon_button(250,135,self.mesprit,"Mesprit",boot_screen)
        self.create_pokemon_button(350,135,self.azelf,"Azelf",boot_screen, True)
        self.create_pokemon_button(450,135,self.heatran,"Heatran",boot_screen, True)
        self.create_pokemon_button(550,135,self.regigigas,"Regigigas",boot_screen, True)
        self.create_pokemon_button(650,135,self.giratina,"Giratina",boot_screen, True)
        self.create_pokemon_button(50,225,self.arceus,"Arceus",boot_screen)
        self.create_pokemon_button(150,225,self.regirock,"Regirock",boot_screen)
        self.create_pokemon_button(250,225,self.registeel,"Registeel",boot_screen)
        self.create_pokemon_button(350,225,self.regice,"Regice",boot_screen, True)
        self.create_pokemon_button(450,225,self.raikou,"Raikou",boot_screen, True)
        self.create_pokemon_button(550,225,self.entei,"Entei",boot_screen, True)
        self.create_pokemon_button(650,225,self.suicune,"Suicune",boot_screen, True)
        self.create_pokemon_button(50,315,self.latias,"Latias",boot_screen)
        self.create_pokemon_button(150,315,self.latios,"Latios",boot_screen)
        self.create_pokemon_button(250,315,self.ho_oh,"Ho-Oh",boot_screen)
        self.create_pokemon_button(350,315,self.kyogre,"Kyogre",boot_screen, True)
        self.create_pokemon_button(450,315,self.groudon,"Groudon",boot_screen, True)
        self.create_pokemon_button(550,315,self.rayquaza,"Rayquaza",boot_screen, True)
        self.create_pokemon_button(650,315,self.mewtwo,"Mewtwo",boot_screen, True)

        # Back button
        back_button = ctk.CTkButton(self,text="Back",font=("Arial",20),width=100,height=40,fg_color="#3b3b3b",hover_color="#505050",command=back_callback)

        back_button.place(x=340,y=420)



    # Start hunt
    def start_hunt(self, pokemon_name, boot_screen):

        config.game_name = "Brilliant Diamond"
        config.pokemon_name = pokemon_name

        boot_screen()



    # Pokemon button creation
    def create_pokemon_button(self,x,y,image,name,boot_screen):

        # Button
        button = ctk.CTkButton(self, image=image, text="", width=80, height=80, fg_color="#5e5e5e", bg_color="#21344a", hover_color="#bfbfbf", border_width=3, border_color="black", corner_radius=10, command=lambda: self.start_hunt(name,boot_screen))

        button.place(x=x,y=y)


        # Name box
        label_box = ctk.CTkFrame(self,fg_color="black",bg_color="#5e5e5e",width=76,height=16,corner_radius=2)

        label_box.place(x=x+8,y=y+60)


        # Name
        label = ctk.CTkLabel(master=label_box,text=name,font=("Arial",9),text_color="black",fg_color="white",width=74,height=14,corner_radius=3)

        label.place(x=1,y=1)


        return button, label