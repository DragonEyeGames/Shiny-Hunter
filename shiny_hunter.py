import tkinter as tk

#Button scripts

def on_click_sword_shield():
    print("Sword and Shield button clicked")

#Initialize the main window
root = tk.Tk()
root.title("Shiny Hunter")
root.geometry("1280x720")

root.attributes('-fullscreen', True)
root.bind('<Escape>', lambda e: root.attributes('-fullscreen', False))

root.configure(bg="#4a4a4a")

#Populate the main window with widgets

label = tk.Label(root, text="Select which game you will be hunting in:", font=("Arial", 24), bg="#4a4a4a", fg="black")
label.pack(pady=20)

button = tk.Button(root, text="SW/SH", bg="#4a4a4a", fg="black", font=("Arial", 18), command=on_click_sword_shield)
button.place(x=50, y=70, width=100, height=100)

root.mainloop()