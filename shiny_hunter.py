import tkinter as tk

root = tk.Tk()
root.title("Shiny Hunter")
root.geometry("1280x720")
root.bind('<Escape>', lambda e: root.attributes('-fullscreen', False))

root.mainloop()