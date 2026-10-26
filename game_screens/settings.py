import customtkinter as ctk
from PIL import Image
import os
import config
from discord_webhook import send_discord_update, send_shiny_notification
import threading
import time

from save_manager import load_settings, save_settings

class SettingsScreen(ctk.CTkFrame):

    def __init__(self, parent, back_callback):
        super().__init__( parent, fg_color="#050c15" )

        title_font = ctk.CTkFont(family="Knewave", size=60)
        subtitle_font = ctk.CTkFont(family="Knewave", size=30)
        instruction_font = ctk.CTkFont(family="Basic", size=22)

        def clear_shiny():
            self.shiny_field.delete(0, "end")

        def clear_normal():
            self.normal_field.delete(0, "end")

        def test_webhooks():
            self.test_button.configure(text="Sent...", state="disabled", text_color="gray50", fg_color="gray25")
            
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
            
            self.test_button.after(2000, reset_test_button)

        def reset_test_button():
            self.test_button.configure(text="Test", state="normal", text_color="white", fg_color="#1fa323", hover_color="#1d8a21")

        def save_webhooks():
            self.save_button.configure(text="Saved...", state="disabled", text_color="gray50", fg_color="gray25")
            save_settings(self.shiny_field.get(), self.normal_field.get())
            self.save_button.after(2000, reset_save_button)
            config.SHINY_URL = self.shiny_field.get()
            config.NONSHINY_URL = self.normal_field.get()

        def reset_save_button():
            self.save_button.configure(text="Save", state="normal", text_color="white", fg_color="#1fa323", hover_color="#1d8a21")

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

        self.shiny_field = ctk.CTkEntry(self, placeholder_text="Input Discord Webhook URL...", width=550, height=40)
        self.shiny_field.place(x=100,y=210)

        clear_button = ctk.CTkButton(self,text="Clear",font=("Basic",25),width=80,height=40,fg_color="#C0392B",hover_color="#96281B",border_color="black",border_width=3,command=clear_shiny, corner_radius=10)
        clear_button.place(x=670,y=210)

        normal_prompt = ctk.CTkLabel(self, text="Input the URL for you Non-Shiny Discord Webhook", font=instruction_font)
        normal_prompt.place(x=100, y=275)

        self.normal_field = ctk.CTkEntry(self, placeholder_text="Input Discord Webhook URL...", width=550, height=40)
        self.normal_field.place(x=100,y=310)

        clear_button = ctk.CTkButton(self,text="Clear",font=("Basic",25),width=80,height=40,fg_color="#C0392B",hover_color="#96281B",border_color="black",border_width=3,command=clear_normal, corner_radius=10)
        clear_button.place(x=670,y=310)

        self.test_button = ctk.CTkButton(self,text="Test",font=("Basic",25),width=100,height=40,fg_color="#1fa323",hover_color="#1d8a21",border_color="black",border_width=3,command=test_webhooks, corner_radius=10)
        self.test_button.place(x=225,y=360)

        self.save_button = ctk.CTkButton(self,text="Save",font=("Basic",25),width=100,height=40,fg_color="#1fa323",hover_color="#1d8a21",border_color="black",border_width=3,command=save_webhooks, corner_radius=10)
        self.save_button.place(x=475,y=360)

        shiny_value, non_shiny_value = load_settings()


        self.shiny_field.delete(0, "end")
        self.shiny_field.insert(0, shiny_value)

        self.normal_field.delete(0, "end")
        self.normal_field.insert(0, non_shiny_value)

        config.SHINY_URL = shiny_value
        config.NONSHINY_URL = non_shiny_value

        