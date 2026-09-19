import customtkinter as ctk
from PIL import Image
import os
import config


class SwScreen(ctk.CTkFrame):

    def __init__(self, parent, back_callback, boot_screen, egg_screen):
        super().__init__( parent, fg_color="#050c15" )

        # Images

        self.size=(80, 80)

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


        box_x, box_y, box_w, box_h = 123, 150, 580, 265
        self.color_box = ctk.CTkFrame(self, fg_color="#21344a", width=box_w, height=box_h,
                                    corner_radius=15, border_width=5, border_color="black")
        self.color_box.place(x=box_x, y=box_y)

        # Button grid geometry
        btn_size = 90
        spacing = 110   # center-to-center spacing between buttons
        row_gap = 10    # vertical gap between the two rows

        def row_start_x(n_buttons):
            total_w = (n_buttons - 1) * spacing + btn_size
            return box_x + (box_w - total_w) // 2

        row1_x = row_start_x(5)   # -> 148
        row2_x = row_start_x(3)   # -> 258

        total_h = 2 * btn_size + row_gap
        row1_y = box_y + (box_h - total_h) // 2   # -> ~188
        row2_y = row1_y + btn_size + row_gap      # -> ~288

        # Pokemon buttons
        self.create_pokemon_button(row1_x + 0*spacing, row1_y, self.regirock,   "Regirock",   boot_screen)
        self.create_pokemon_button(row1_x + 1*spacing, row1_y, self.regice,     "Regice",     boot_screen)
        self.create_pokemon_button(row1_x + 2*spacing, row1_y, self.registeel,  "Registeel",  boot_screen)
        self.create_pokemon_button(row1_x + 3*spacing, row1_y, self.regieleki,  "Regieleki",  boot_screen)
        self.create_pokemon_button(row1_x + 4*spacing, row1_y, self.regidrago,  "Regidrago",  boot_screen, True)

        self.create_pokemon_button(row2_x + 0*spacing, row2_y, self.cobalion,   "Cobalion",   boot_screen, True)
        self.create_pokemon_button(row2_x + 1*spacing, row2_y, self.terrakion,  "Terrakion",  boot_screen, True)
        self.create_pokemon_button(row2_x + 2*spacing, row2_y, self.virizion,   "Virizion",   boot_screen, True)

        #Masuda selection screen
        self.egg_button = ctk.CTkButton(self,
            text="Overworld Encounter",
            width=180, height=40,
            fg_color="#5e5e5e", bg_color="#050c15", hover_color="#bfbfbf",
            border_width=3, border_color="black", corner_radius=10,
            font=("Arial", 20),
            command=lambda: self.start_egg(egg_screen))
        self.egg_button.place(x=310, y=360)

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


    # Pokemon button creation
    def create_pokemon_button(self,x,y,image,name,boot_screen, disabled=False):

        # Button
        button = ctk.CTkButton(self, image=image, text="", width=90, height=90, fg_color="#5e5e5e", bg_color="#21344a", hover_color="#bfbfbf", border_width=3, border_color="black", corner_radius=10, command=lambda: self.start_hunt(name,boot_screen))

        button.place(x=x,y=y)

        if(disabled):
            button.configure(state="disabled")

        # Name box
        label_box = ctk.CTkFrame(self,fg_color="black",bg_color="#5e5e5e",width=86,height=20,corner_radius=5)

        label_box.place(x=x+8,y=y+66)


        # Name
        label = ctk.CTkLabel(master=label_box,text=name,font=("Arial",14),text_color="black",fg_color="white",width=84,height=20,corner_radius=3)

        label.place(x=1,y=1)


        return button, label