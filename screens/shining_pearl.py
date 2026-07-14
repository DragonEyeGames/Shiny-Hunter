import customtkinter as ctk
from PIL import Image

import config


class SpScreen(ctk.CTkFrame):

    def __init__(self, parent, back_callback, boot_screen):
        super().__init__( parent, fg_color="#050c15" )

        # Images
        self.giratina = ctk.CTkImage(light_image=Image.open("pokemon/giratina.png"),dark_image=Image.open("pokemon/giratina.png"),size=(70,70))

        self.arceus = ctk.CTkImage(light_image=Image.open("pokemon/arceus.png"),dark_image=Image.open("pokemon/arceus.png"),size=(70,70))


        # Title
        title = ctk.CTkLabel(self,text="Pokemon Shining Pearl",font=("Arial", 35, "bold"),text_color="#2b89d9")

        title.pack(pady=(25, 10))


        # Subtitle
        label = ctk.CTkLabel(self,text="Select a Pokemon to Hunt",font=("Arial", 20),text_color="white")

        label.pack()


        # Outline box
        self.color_box = ctk.CTkFrame(self,fg_color="#21344a",width=594,height=194,corner_radius=15, border_width=5, border_color="black")

        self.color_box.place(x=103,y=170)


        # Pokemon buttons
        self.create_pokemon_button(113,180,self.giratina,"Giratina",boot_screen)

        self.create_pokemon_button(213,180,self.arceus,"Arceus",boot_screen)


        # Back button
        back_button = ctk.CTkButton(self,text="Back",font=("Arial",20),width=100,height=40,fg_color="#3b3b3b",hover_color="#505050",command=back_callback)

        back_button.place(x=340,y=420)



    # Start hunt
    def start_hunt(self, pokemon_name, boot_screen):

        config.game_name = "Shining Pearl"
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