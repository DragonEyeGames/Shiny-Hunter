import customtkinter as ctk
from PIL import Image
import os
import config


class SettingsScreen(ctk.CTkFrame):

    def __init__(self, parent, back_callback):
        super().__init__( parent, fg_color="#050c15" )

        title_font = ctk.CTkFont(family="Knewave", size=60)
        subtitle_font = ctk.CTkFont(family="Knewave", size=30)

        # Title
        title = ctk.CTkLabel(self,text=" Settings ",font=title_font,text_color="#3d9beb")

        title.pack(pady=(5, 0))


        # Subtitle
        label = ctk.CTkLabel(self,text=" Select a Setting to Change ",font=subtitle_font,text_color="white")

        label.pack()

        # Back button
        back_button = ctk.CTkButton(self,text="Back",font=("Basic",25),width=100,height=40,fg_color="#C0392B",hover_color="#96281B",border_color="black",border_width=3,command=back_callback, corner_radius=10)

        back_button.place(x=350,y=430)

        self.input_field = ctk.CTkEntry(self.popup_button, placeholder_text="Input Discord Webhook URL...", width=600, height=40)
        self.input_field.place(x=100,y=200)