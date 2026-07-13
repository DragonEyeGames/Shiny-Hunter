import tkinter as tk

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
root = tk.Tk()
root.title("Shiny Hunter")
root.geometry("800x480")

root.attributes('-fullscreen', True)

def toggle_fullscreen(event=None):
    root.attributes("-fullscreen", not root.attributes("-fullscreen"))

root.bind("<Escape>", toggle_fullscreen)

root.configure(bg="#2b2b2b")

#Boot up screens

def open_capture_screen():
    config.start_camera=True
    switch_screen.tkraise()

def close_project():
    save_data(config.hunting_data)
    root.destroy()

main_menu = tk.Frame(root, bg="#2b2b2b")
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

#Populate the main window with widgets

sword = tk.PhotoImage(file="logos/sword.png")
selected_sword = tk.PhotoImage(file="logos/selected_sword.png")

shield = tk.PhotoImage(file="logos/shield.png")
selected_shield = tk.PhotoImage(file="logos/selected_shield.png")

brilliant_diamond = tk.PhotoImage(file="logos/brilliant_diamond.png")
selected_brilliant_diamond = tk.PhotoImage(file="logos/selected_brilliant_diamond.png")


shining_pearl = tk.PhotoImage(file="logos/shining_pearl.png")
selected_shining_pearl = tk.PhotoImage(file="logos/selected_shining_pearl.png")

eevee = tk.PhotoImage(file="logos/eevee.png")
selected_eevee = tk.PhotoImage(file="logos/selected_eevee.png")

pikachu = tk.PhotoImage(file="logos/pikachu.png")
selected_pikachu = tk.PhotoImage(file="logos/selected_pikachu.png")

fire_red = tk.PhotoImage(file="logos/fire_red.png")
selected_fire_red = tk.PhotoImage(file="logos/selected_fire_red.png")

leaf_green = tk.PhotoImage(file="logos/leaf_green.png")
selected_leaf_green = tk.PhotoImage(file="logos/selected_leaf_green.png")

label = tk.Label(main_menu, text="Pokemon Shiny Hunter", font=("Droid Sans Fallback", 35), bg="#2b2b2b", fg="white")
label.pack(pady=18)

label = tk.Label(main_menu, text="Pick a Game to Hunt In", font=("Droid Sans Fallback", 24), bg="#2b2b2b", fg="white")
label.pack()

lets_go_eevee_button = tk.Button(main_menu, image=eevee, bg="#bfbfbf", command=on_click_lets_go_eevee)
lets_go_eevee_button.place(x=100, y=160, width=100, height=100)

lets_go_eevee_button.bind("<Enter>", lambda event: lets_go_eevee_button.config(image=selected_eevee))
lets_go_eevee_button.bind("<Leave>", lambda event: lets_go_eevee_button.config(image=eevee))

lets_go_pikachu_button = tk.Button(main_menu, image=pikachu, bg="#bfbfbf", command=on_click_lets_go_pikachu)
lets_go_pikachu_button.place(x=100, y=280, width=100, height=100)

lets_go_pikachu_button.bind("<Enter>", lambda event: lets_go_pikachu_button.config(image=selected_pikachu))
lets_go_pikachu_button.bind("<Leave>", lambda event: lets_go_pikachu_button.config(image=pikachu))

sword_button = tk.Button(main_menu, bg="#bfbfbf", image=sword, command=on_click_sword)
sword_button.place(x=250, y=160, width=100, height=100)

sword_button.bind("<Enter>", lambda event: sword_button.config(image=selected_sword))
sword_button.bind("<Leave>", lambda event: sword_button.config(image=sword))

shield_button = tk.Button(main_menu, bg="#bfbfbf", image=shield, command=on_click_shield)
shield_button.place(x=250, y=280, width=100, height=100)

shield_button.bind("<Enter>", lambda event: shield_button.config(image=selected_shield))
shield_button.bind("<Leave>", lambda event: shield_button.config(image=shield))


brilliant_diamond_button = tk.Button(main_menu, bg="#bfbfbf", image=brilliant_diamond, command=on_click_brilliant_diamond)
brilliant_diamond_button.place(x=400, y=160, width=100, height=100)

brilliant_diamond_button.bind("<Enter>", lambda event: brilliant_diamond_button.config(image=selected_brilliant_diamond))
brilliant_diamond_button.bind("<Leave>", lambda event: brilliant_diamond_button.config(image=brilliant_diamond))

shining_pearl_button = tk.Button(main_menu, text="Sp", bg="#bfbfbf", image=shining_pearl, command=on_click_shining_pearl)
shining_pearl_button.place(x=400, y=280, width=100, height=100)

shining_pearl_button.bind("<Enter>", lambda event: shining_pearl_button.config(image=selected_shining_pearl))
shining_pearl_button.bind("<Leave>", lambda event: shining_pearl_button.config(image=shining_pearl))

red_button = tk.Button(main_menu, bg="#bfbfbf", image=fire_red, command=on_click_fire_red)
red_button.place(x=550, y=160, width=100, height=100)

red_button.bind("<Enter>", lambda event: red_button.config(image=selected_fire_red))
red_button.bind("<Leave>", lambda event: red_button.config(image=fire_red))

green_button = tk.Button(main_menu, bg="#bfbfbf", image=leaf_green, command=on_click_leaf_green)
green_button.place(x=550, y=280, width=100, height=100)

green_button.bind("<Enter>", lambda event: green_button.config(image=selected_leaf_green))
green_button.bind("<Leave>", lambda event: green_button.config(image=leaf_green))

end_button = tk.Button(main_menu, text="Quit Program", font=("C052", 16), command=close_project)
end_button.place(x=265, y=420, width=230, height=40)


root.mainloop()