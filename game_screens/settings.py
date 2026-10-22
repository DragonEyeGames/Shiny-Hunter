import customtkinter as ctk
from PIL import Image
import os
import config
from discord_webhook import send_discord_update, send_shiny_notification
import threading

class SettingsScreen(ctk.CTkFrame):

    def __init__(self, parent, back_callback):
        super().__init__( parent, fg_color="#050c15" )

        title_font = ctk.CTkFont(family="Knewave", size=60)
        subtitle_font = ctk.CTkFont(family="Knewave", size=30)
        instruction_font = ctk.CTkFont(family="Basic", size=22)

        # Title
        title = ctk.CTkLabel(self,text=" Settings ",font=title_font,text_color="#3d9beb")

        title.pack(pady=(5, 0))


        # Subtitle
        label = ctk.CTkLabel(self,text=" Select a Setting to Change ",font=subtitle_font,text_color="white")

        label.pack()

        # Back button
        back_button = ctk.CTkButton(self,text="Back",font=("Basic",25),width=100,height=40,fg_color="#C0392B",hover_color="#96281B",border_color="black",border_width=3,command=back_callback, corner_radius=10)

        back_button.place(x=350,y=430)

        shiny_prompt = ctk.CTkLabel(self, text="Input the URL for you Shiny Discord Webhook", font=instruction_font)
        shiny_prompt.place(x=100, y=175)

        self.shiny_field = ctk.CTkEntry(self, placeholder_text="Input Discord Webhook URL...", width=600, height=40)
        self.shiny_field.place(x=100,y=210)

        normal_prompt = ctk.CTkLabel(self, text="Input the URL for you Non-Shiny Discord Webhook", font=instruction_font)
        normal_prompt.place(x=100, y=275)

        self.normal_field = ctk.CTkEntry(self, placeholder_text="Input Discord Webhook URL...", width=600, height=40)
        self.normal_field.place(x=100,y=310)

        test_button = ctk.CTkButton(self,text="Test",font=("Basic",25),width=100,height=40,fg_color="#1fa323",hover_color="#1d8a21",border_color="black",border_width=3,command=test_webhooks, corner_radius=10)

        test_button.place(x=175,y=360)

        save_button = ctk.CTkButton(self,text="Test",font=("Basic",25),width=100,height=40,fg_color="#1fa323",hover_color="#1d8a21",border_color="black",border_width=3,command=back_callback, corner_radius=10)

        save_button.place(x=625,y=360)

        def test_webhooks():
            threading.Thread(
                target=send_discord_update,
                args=(f"The shiny webhook works!", self.shiny_field.get()),
                daemon=True
            ).start()
            threading.Thread(
                target=send_discord_update,
                args=(f"The non-shiny webhook works!", self.normal_field.get()),
                daemon=True
            ).start()