import customtkinter as ctk
from PIL import Image

from screens.sword import SwScreen
from screens.shield import ShScreen
from screens.brilliant_diamond import BdScreen
from screens.shining_pearl import SpScreen
from screens.fire_red import FrScreen
from screens.leaf_green import LgScreen
from screens.lets_go_eevee import LgeScreen
from screens.lets_go_pikachu import LgpScreen

from capture_card import CaptureCard
import config
from save_manager import save_data

#Initialize the main window
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("Shiny Hunter")
root.geometry("800x480")
root.attributes("-fullscreen", True)

def toggle_fullscreen(event=None):
    root.attributes("-fullscreen", not root.attributes("-fullscreen"))

root.bind("<Escape>", toggle_fullscreen)

root.configure(bg="#050c15")

#Boot up screens

def open_capture_screen():
    config.start_camera=True
    switch_screen.tkraise()

def close_project():
    save_data(config.hunting_data)
    root.destroy()

main_menu = ctk.CTkFrame(root,fg_color="#050c15",corner_radius=0)
main_menu.place(x=0, y=0, relwidth=1, relheight=1)

switch_screen = CaptureCard(root, lambda: main_menu.tkraise(), camera_index=0)
switch_screen.place(x=0, y=0, relwidth=1, relheight=1)

sw = SwScreen(root, lambda: main_menu.tkraise(), open_capture_screen)
sw.place(x=0, y=0, relwidth=1, relheight=1)

sh = ShScreen(root, lambda: main_menu.tkraise(), open_capture_screen)
sh.place(x=0, y=0, relwidth=1, relheight=1)

bd = BdScreen(root, lambda: main_menu.tkraise(), open_capture_screen)
bd.place(x=0, y=0, relwidth=1, relheight=1)

sp = SpScreen(root, lambda: main_menu.tkraise(), open_capture_screen)
sp.place(x=0, y=0, relwidth=1, relheight=1)

fr = FrScreen(root, lambda: main_menu.tkraise())
fr.place(x=0, y=0, relwidth=1, relheight=1)

lg = LgScreen(root, lambda: main_menu.tkraise())
lg.place(x=0, y=0, relwidth=1, relheight=1)

lge = LgeScreen(root, lambda: main_menu.tkraise())
lge.place(x=0, y=0, relwidth=1, relheight=1)

lgp = LgpScreen(root, lambda: main_menu.tkraise())
lgp.place(x=0, y=0, relwidth=1, relheight=1)

main_menu.tkraise()

#Button scripts

def on_click_sword():
    sw.tkraise()

def on_click_shield():
    sh.tkraise()

def on_click_lets_go_eevee():
    lge.tkraise()

def on_click_lets_go_pikachu():
    lgp.tkraise()

def on_click_brilliant_diamond():
    bd.tkraise()

def on_click_shining_pearl():
    sp.tkraise()

def on_click_fire_red():
    fr.tkraise()

def on_click_leaf_green():
    lg.tkraise()

#Button helper function
def create_game_button(parent, x, y, image, hover_image, command):
    button = ctk.CTkButton(
        parent,
        image=image,
        text="",
        width=100,
        height=100,
        fg_color="#bfbfbf",
        hover_color="#bfbfbf",
        border_color="black",
        border_width=3,
        corner_radius=12,
        command=command
    )

    button.place(x=x, y=y)

    button.bind("<Enter>", lambda e: button.configure(image=hover_image))
    button.bind("<Leave>", lambda e: button.configure(image=image))

    return button

#Populate the main window with widgets

sword = ctk.CTkImage(light_image=Image.open("logos/sword.png"), dark_image=Image.open("logos/sword.png"), size=(100,100) )
selected_sword = ctk.CTkImage(light_image=Image.open("logos/selected_sword.png"), dark_image=Image.open("logos/selected_sword.png"), size=(100,100) )

shield = ctk.CTkImage(light_image=Image.open("logos/shield.png"), dark_image=Image.open("logos/shield.png"), size=(100,100) )
selected_shield = ctk.CTkImage(light_image=Image.open("logos/selected_shield.png"), dark_image=Image.open("logos/selected_shield.png"), size=(100,100) )

brilliant_diamond = ctk.CTkImage(light_image=Image.open("logos/brilliant_diamond.png"), dark_image=Image.open("logos/brilliant_diamond.png"), size=(100,100) )
selected_brilliant_diamond = ctk.CTkImage(light_image=Image.open("logos/selected_brilliant_diamond.png"), dark_image=Image.open("logos/selected_brilliant_diamond.png"), size=(100,100) )

shining_pearl = ctk.CTkImage(light_image=Image.open("logos/shining_pearl.png"), dark_image=Image.open("logos/shining_pearl.png"), size=(100,100) )
selected_shining_pearl = ctk.CTkImage(light_image=Image.open("logos/selected_shining_pearl.png"), dark_image=Image.open("logos/selected_shining_pearl.png"), size=(100,100) )

eevee = ctk.CTkImage(light_image=Image.open("logos/eevee.png"), dark_image=Image.open("logos/eevee.png"), size=(100,100) )
selected_eevee = ctk.CTkImage(light_image=Image.open("logos/selected_eevee.png"), dark_image=Image.open("logos/selected_eevee.png"), size=(100,100) )

pikachu = ctk.CTkImage(light_image=Image.open("logos/pikachu.png"),dark_image=Image.open("logos/pikachu.png"),size=(100,100))
selected_pikachu = ctk.CTkImage(light_image=Image.open("logos/selected_pikachu.png"),dark_image=Image.open("logos/selected_pikachu.png"),size=(100,100))

fire_red = ctk.CTkImage(light_image=Image.open("logos/fire_red.png"),dark_image=Image.open("logos/fire_red.png"),size=(100,100))
selected_fire_red = ctk.CTkImage(light_image=Image.open("logos/selected_fire_red.png"),dark_image=Image.open("logos/selected_fire_red.png"),size=(100,100))

leaf_green = ctk.CTkImage(light_image=Image.open("logos/leaf_green.png"),dark_image=Image.open("logos/leaf_green.png"),size=(100,100))
selected_leaf_green = ctk.CTkImage(light_image=Image.open("logos/selected_leaf_green.png"),dark_image=Image.open("logos/selected_leaf_green.png"),size=(100,100))

title = ctk.CTkLabel(
    main_menu,
    text="Pokémon Shiny Hunter",
    font=("Arial",40,"bold"),
    text_color="#2b89d9"
)

title.pack(pady=(25,5))

subtitle = ctk.CTkLabel(
    main_menu,
    text="Select a Game",
    font=("Arial",25)
)

subtitle.pack()

color_box = ctk.CTkFrame(main_menu,fg_color="#21344a",width=610,height=272,corner_radius=15, border_width=5, border_color="black")

color_box.place(x=90,y=130)

#Create the game buttons with a consistent theme in mind.

create_game_button(main_menu, 100, 140, eevee, selected_eevee, on_click_lets_go_eevee)

create_game_button(main_menu, 100, 260, pikachu, selected_pikachu, on_click_lets_go_pikachu)

create_game_button(main_menu, 250, 140, sword, selected_sword, on_click_sword)

create_game_button(main_menu, 250, 260, shield, selected_shield, on_click_shield)

create_game_button(main_menu, 400, 140, brilliant_diamond, selected_brilliant_diamond, on_click_brilliant_diamond)

create_game_button(main_menu, 400, 260, shining_pearl, selected_shining_pearl, on_click_shining_pearl)

create_game_button(main_menu, 550, 140, fire_red, selected_fire_red, on_click_fire_red)

create_game_button(main_menu, 550, 260, leaf_green, selected_leaf_green, on_click_leaf_green)

#The button to close down the program
end_button = ctk.CTkButton(main_menu,text="Quit Program",width=230,height=40,fg_color="#C0392B",hover_color="#96281B", border_width=2, border_color="black", corner_radius=12,font=("Arial",16,"bold"),command=close_project)
end_button.place(x=285, y=420)


root.mainloop()