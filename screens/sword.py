import customtkinter as ctk
from PIL import Image
import os
import config


class SwScreen(ctk.CTkFrame):

    def __init__(self, parent, back_callback, boot_screen, egg_screen):
        super().__init__( parent, fg_color="#050c15" )

        # Images

        self.size=(70, 70)

        self.regirock = ctk.CTkImage(light_image=Image.open("pokemon/regirock.png"),dark_image=Image.open("pokemon/regirock.png"),size=self.size)
        self.registeel = ctk.CTkImage(light_image=Image.open("pokemon/registeel.png"),dark_image=Image.open("pokemon/registeel.png"),size=self.size)
        self.regice = ctk.CTkImage(light_image=Image.open("pokemon/regice.png"),dark_image=Image.open("pokemon/regice.png"),size=self.size)
        self.regidrago = ctk.CTkImage(light_image=Image.open("pokemon/regidrago.png"),dark_image=Image.open("pokemon/regidrago.png"),size=self.size)
        self.regieleki = ctk.CTkImage(light_image=Image.open("pokemon/regieleki.png"),dark_image=Image.open("pokemon/regieleki.png"),size=self.size)
        self.virizion = ctk.CTkImage(light_image=Image.open("pokemon/virizion.png"),dark_image=Image.open("pokemon/virizion.png"),size=self.size)
        self.terrakion = ctk.CTkImage(light_image=Image.open("pokemon/terrakion.png"),dark_image=Image.open("pokemon/terrakion.png"),size=self.size)
        self.cobalion = ctk.CTkImage(light_image=Image.open("pokemon/cobalion.png"),dark_image=Image.open("pokemon/cobalion.png"),size=self.size)
        self.arctovish = ctk.CTkImage(light_image=Image.open("pokemon/arctovish.png"),dark_image=Image.open("pokemon/arctovish.png"),size=self.size)
        self.arctozolt = ctk.CTkImage(light_image=Image.open("pokemon/arctozolt.png"),dark_image=Image.open("pokemon/arctozolt.png"),size=self.size)
        self.dracovish = ctk.CTkImage(light_image=Image.open("pokemon/dracovish.png"),dark_image=Image.open("pokemon/dracovish.png"),size=self.size)
        self.dracozolt = ctk.CTkImage(light_image=Image.open("pokemon/dracozolt.png"),dark_image=Image.open("pokemon/dracozolt.png"),size=self.size)
        self.egg = ctk.CTkImage(light_image=Image.open("pokemon/egg.png"),dark_image=Image.open("pokemon/egg.png"),size=(36,44))

        title_font = ctk.CTkFont(family="Knewave", size=60)
        subtitle_font = ctk.CTkFont(family="Knewave", size=30)

        # Title
        title = ctk.CTkLabel(self,text=" Pokémon Sword ",font=title_font,text_color="#2b89d9")

        title.pack(pady=(5, 0))


        # Subtitle
        label = ctk.CTkLabel(self,text=" Select a Pokémon to Hunt ",font=subtitle_font,text_color="white")

        label.pack()


        # Outline box
        self.color_box = ctk.CTkFrame(self,fg_color="#21344a",width=500,height=250,corner_radius=15, border_width=5, border_color="black")

        self.color_box.place(x=150,y=160)


        # Pokemon buttons
        self.create_pokemon_button(150,160,self.regirock,"Regirock",boot_screen)
        self.create_pokemon_button(250,160,self.regice,"Regice",boot_screen)
        self.create_pokemon_button(350,160,self.registeel,"Registeel",boot_screen)
        self.create_pokemon_button(450,160,self.regieleki,"Regieleki",boot_screen)
        self.create_pokemon_button(550,160,self.regidrago,"Regidrago",boot_screen, True)
        self.create_pokemon_button(250,260,self.cobalion,"Cobalion",boot_screen, True)
        self.create_pokemon_button(350,260,self.terrakion,"Terrakion",boot_screen, True)
        self.create_pokemon_button(450,260,self.virizion,"Virizion",boot_screen, True)

        #Masuda selection screen
        self.egg_button = ctk.CTkButton(self,
            text="Overworld Encounter",
            width=180, height=40,
            fg_color="#5e5e5e", bg_color="#21344a", hover_color="#bfbfbf",
            border_width=3, border_color="black", corner_radius=10,
            font=("Arial", 20),
            command=lambda: self.start_egg(egg_screen))
        self.egg_button.place(x=310, y=361)

        # Back button
        back_button = ctk.CTkButton(self,text="Back",font=("Arial",20),width=100,height=40,fg_color="#3b3b3b",hover_color="#505050",border_color="black",border_width=3,command=back_callback)

        back_button.place(x=350,y=430)



    # Start hunt
    def start_hunt(self, pokemon_name, boot_screen):

        config.game_name = "Sword"
        config.pokemon_name = pokemon_name

        boot_screen()

    def start_egg(self, egg_screen):
        config.game_name = "Sword"
        egg_screen()


    def create_pokemon_button(self, x, y, image, name, boot_screen, disabled=False):

        # Button (80x80 size, placed at x+10, y+10)
        button = ctk.CTkButton(self, image=image, text="", width=80, border_spacing=0, fg_color="#5e5e5e", bg_color="#21344a", hover_color="#bfbfbf", command=lambda: self.start_hunt(name,boot_screen))
        button.place(x=x+10, y=y+10)

        if disabled:
            button.configure(state="disabled")

        # Name box (Width matches the inner button area, perfectly centered at the bottom)
        label_box = ctk.CTkFrame(self, fg_color="black", bg_color="#5e5e5e", width=74, height=18, corner_radius=5)
        label_box.place(x=x+23, y=y+70) # Centers horizontally, flushes close to the bottom border

        # Name (Fits snugly inside the black label_box frame)
        label = ctk.CTkLabel(master=label_box, text=name, font=("Arial",11), text_color="black", fg_color="white", width=72, height=18, corner_radius=3)
        label.place(x=1, y=1)

        self.update_idletasks()
        print(button.winfo_width(), button.winfo_height())

        return button, label