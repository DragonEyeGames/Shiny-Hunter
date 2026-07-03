import tkinter as tk
from sw_sh import SwShScreen


#Initialize the main window
root = tk.Tk()
root.title("Shiny Hunter")
root.geometry("1280x720")

root.attributes('-fullscreen', True)
root.bind('<Escape>', lambda e: root.attributes('-fullscreen', False))

root.configure(bg="#4a4a4a")

#Boot up screens

main_menu = tk.Frame(root, bg="#4a4a4a")
main_menu.place(x=0, y=0, relwidth=1, relheight=1)

swsh = SwShScreen(root)
swsh.place(x=0, y=0, relwidth=1, relheight=1)

main_menu.tkraise()

#Button scripts

def on_click_sword_shield():
    print("Sword and Shield button clicked")
    swsh.tkraise()

def on_click_lets_go():
    print("Let's go button clicked")

def on_click_diamond_pearl():
    print("Diamond and Pearl button clicked")

def on_click_red_green():
    print("Red and Green button clicked")

#Populate the main window with widgets

label = tk.Label(main_menu, text="Select which game you will be hunting in:", font=("Arial", 24), bg="#4a4a4a", fg="black")
label.pack(pady=20)

lets_go_button = tk.Button(main_menu, text="Let's Go", bg="#bfbfbf", fg="black", font=("Arial", 18), command=on_click_lets_go)
lets_go_button.place(x=50, y=70, width=100, height=100)

sword_shield_button = tk.Button(main_menu, text="SW/SH", bg="#bfbfbf", fg="black", font=("Arial", 18), command=on_click_sword_shield)
sword_shield_button.place(x=200, y=70, width=100, height=100)

diamond_pearl_button = tk.Button(main_menu, text="Bd/Sp", bg="#bfbfbf", fg="black", font=("Arial", 18), command=on_click_diamond_pearl)
diamond_pearl_button.place(x=350, y=70, width=100, height=100)

red_green_button = tk.Button(main_menu, text="Fr/Lg", bg="#bfbfbf", fg="black", font=("Arial", 18), command=on_click_red_green)
red_green_button.place(x=500, y=70, width=100, height=100)

root.mainloop()