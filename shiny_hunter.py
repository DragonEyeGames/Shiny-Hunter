import tkinter as tk


#Initialize the main window
root = tk.Tk()
root.title("Shiny Hunter")
root.geometry("1280x720")

root.attributes('-fullscreen', True)
root.bind('<Escape>', lambda e: root.attributes('-fullscreen', False))

root.configure(bg="#4a4a4a")

#Populate the main window with widgets

label = tk.Label(root, text="Select which game you will be hunting in:", font=("Arial", 24))
label.pack(pady=20)

root.mainloop()