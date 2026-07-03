import tkinter as tk

class SwShScreen(tk.Frame):
    def __init__(self, parent, back_callback):
        super().__init__(parent, bg="#4a4a4a")

        self.regirock = tk.PhotoImage(file="images/regirock.png")
        self.regice = tk.PhotoImage(file="images/regice.png")

        #Game title
        label = tk.Label(
            self,
            text="Sword and Shield",
            font=("Arial", 30),
            bg="#4a4a4a"
        )
        label.pack(pady=20)

        #Text for the user to select a pokemon
        label = tk.Label(
            self,
            text="Select the pokemon you want to hunt:",
            font=("Arial", 24),
            bg="#4a4a4a"
        )
        label.place(x=70, y=80)

        #Regirock button and text

        regirock_button = tk.Button(
            self,
            image=self.regirock,
            bg="#8f8d8d",
            activebackground="#bfbfbf",
            borderwidth=0
        )
        regirock_button.place(x=50, y=150, width=70, height=70)

        regirock_text = tk.Label(
            self,
            text="Regirock",
            font=("Arial", 10),
            fg="black",
            bg="white"
        )
        regirock_text.place(x=50, y=200, width=70, height=20)

        #Regice button and text

        regice_button = tk.Button(
            self,
            image=self.regice,
            bg="#8f8d8d",
            activebackground="#bfbfbf",
            borderwidth=0
        )
        regice_button.place(x=150, y=150, width=70, height=70)

        regice_text = tk.Label(
            self,
            text="Regice",
            font=("Arial", 10),
            fg="black",
            bg="white"
        )
        regice_text.place(x=150, y=200, width=70, height=20)

        #Back button

        back_button = tk.Button(
            self,
            text="Back",
            font=("Arial", 15),
            command=back_callback
        )
        back_button.place(x=620, y=650, width=40, height=20)