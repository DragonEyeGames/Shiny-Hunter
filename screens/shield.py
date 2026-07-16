import customtkinter as ctk
from PIL import Image

import config


class ShScreen(ctk.CTkFrame):

    def __init__(self, parent, back_callback, boot_screen):
        super().__init__( parent, fg_color="#050c15" )

        # Images
        self.regirock = ctk.CTkImage(light_image=Image.open("pokemon/regirock.png"),dark_image=Image.open("pokemon/regirock.png"),size=(70,70))
        self.registeel = ctk.CTkImage(light_image=Image.open("pokemon/registeel.png"),dark_image=Image.open("pokemon/registeel.png"),size=(70,70))
        self.regice = ctk.CTkImage(light_image=Image.open("pokemon/regice.png"),dark_image=Image.open("pokemon/regice.png"),size=(70,70))
        self.regidrago = ctk.CTkImage(light_image=Image.open("pokemon/regidrago.png"),dark_image=Image.open("pokemon/regidrago.png"),size=(70,70))
        self.regieleki = ctk.CTkImage(light_image=Image.open("pokemon/regieleki.png"),dark_image=Image.open("pokemon/regieleki.png"),size=(70,70))
        self.virizion = ctk.CTkImage(light_image=Image.open("pokemon/virizion.png"),dark_image=Image.open("pokemon/virizion.png"),size=(70,70))
        self.terrakion = ctk.CTkImage(light_image=Image.open("pokemon/terrakion.png"),dark_image=Image.open("pokemon/terrakion.png"),size=(70,70))
        self.cobalion = ctk.CTkImage(light_image=Image.open("pokemon/cobalion.png"),dark_image=Image.open("pokemon/cobalion.png"),size=(70,70))
        self.arctovish = ctk.CTkImage(light_image=Image.open("pokemon/arctovish.png"),dark_image=Image.open("pokemon/arctovish.png"),size=(70,70))
        self.arctozolt = ctk.CTkImage(light_image=Image.open("pokemon/arctozolt.png"),dark_image=Image.open("pokemon/arctozolt.png"),size=(70,70))
        self.dracovish = ctk.CTkImage(light_image=Image.open("pokemon/dracovish.png"),dark_image=Image.open("pokemon/dracovish.png"),size=(70,70))
        self.dracozolt = ctk.CTkImage(light_image=Image.open("pokemon/dracozolt.png"),dark_image=Image.open("pokemon/dracozolt.png"),size=(70,70))


        # Title
        title = ctk.CTkLabel(self,text="Pokemon Shield",font=("Arial", 35, "bold"),text_color="#2b89d9")

        title.pack(pady=(25, 10))


        # Subtitle
        label = ctk.CTkLabel(self,text="Select a Pokemon to Hunt",font=("Arial", 20),text_color="white")

        label.pack()


        # Outline box
        self.color_box = ctk.CTkFrame(self,fg_color="#21344a",width=614,height=194,corner_radius=15, border_width=5, border_color="black")

        self.color_box.place(x=93,y=170)


        # Pokemon buttons
        self.create_pokemon_button(103,180,self.regirock,"Regirock",boot_screen)
        self.create_pokemon_button(203,180,self.regice,"Regice",boot_screen)
        self.create_pokemon_button(303,180,self.registeel,"Registeel",boot_screen)
        self.create_pokemon_button(403,180,self.regidrago,"Regidrago",boot_screen)
        self.create_pokemon_button(503,180,self.regieleki,"Regieleki",boot_screen, True)
        self.create_pokemon_button(603,180,self.virizion,"Virizion",boot_screen, True)
        self.create_pokemon_button(103,270,self.terrakion,"Terrakion",boot_screen, True)
        self.create_pokemon_button(203,270,self.cobalion,"Cobalion",boot_screen, True)
        self.create_pokemon_button(303,270,self.arctovish,"Arctovish",boot_screen, True)
        self.create_pokemon_button(403,270,self.arctozolt,"Arctozolt",boot_screen, True)
        self.create_pokemon_button(503,270,self.dracovish,"Dracovish",boot_screen, True)
        self.create_pokemon_button(603,270,self.dracozolt,"Dracozolt",boot_screen, True)


        # Back button
        back_button = ctk.CTkButton(self,text="Back",font=("Arial",20),width=100,height=40,fg_color="#3b3b3b",hover_color="#505050",command=back_callback)

        back_button.place(x=340,y=420)



    # Start hunt
    def start_hunt(self, pokemon_name, boot_screen):

        config.game_name = "Shield"
        config.pokemon_name = pokemon_name

        boot_screen()



    # Pokemon button creation
    def create_pokemon_button(self,x,y,image,name,boot_screen, disabled=False):

        # Button
        button = ctk.CTkButton(self, image=image, text="", width=80, height=80, fg_color="#5e5e5e", bg_color="#21344a", hover_color="#bfbfbf", border_width=3, border_color="black", corner_radius=10, command=lambda: self.start_hunt(name,boot_screen))

        button.place(x=x,y=y)

        if(disabled):
            button.configure(state="disabled")

        # Name box
        label_box = ctk.CTkFrame(self,fg_color="black",bg_color="#5e5e5e",width=76,height=16,corner_radius=2)

        label_box.place(x=x+8,y=y+60)


        # Name
        label = ctk.CTkLabel(master=label_box,text=name,font=("Arial",9),text_color="black",fg_color="white",width=74,height=14,corner_radius=3)

        label.place(x=1,y=1)


        return button, label