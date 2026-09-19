import customtkinter as ctk
import cv2
from PIL import Image, ImageTk
import config
from switch_controller import SwitchController
import threading
import time

#Hunting imports
from hunting.sw_sh_registeel import commands as registeel_commands
from hunting.sw_sh_regirock import commands as regirock_commands
from hunting.sw_sh_regidrago import commands as regidrago_commands
from hunting.sw_sh_regice import commands as regice_commands

from hunting.bd_sp_giratina import commands as giratina_commands
from hunting.bd_sp_arceus import commands as arceus_commands

import hunting.bd_sp_hunting_manager as bd_sp_hm
import hunting.sw_sh_hunting_manager as sw_sh_hm

from save_manager import save_data, load_data

class CaptureCard(ctk.CTkFrame):
    def __init__(self, parent, back_callback, camera_index=0):
        super().__init__(parent, fg_color="#050c15")
        self.callback=back_callback

        self.frame_count = 0
        self.camera_started=False

        self.start_time = time.time()
        self.initialize_time = self.start_time

        #Load up the templates for finding the home screen
        self.bd_template = cv2.imread("games/bd_logo.png", cv2.IMREAD_GRAYSCALE)

        def end_hunt():
            print("ending hunt")
            config.status="Ending Hunt"
            self.stop_camera()


        self.color_box = ctk.CTkFrame(self, fg_color="#5e5e5e", width=788, height=208, corner_radius=10, border_color="black", border_width=4)
        self.color_box.pack_propagate(False)
        self.color_box.place(x = 6, y = 146)

        self.border_box = ctk.CTkFrame(self, fg_color="black", width=306, height=186, corner_radius=0)
        self.border_box.pack_propagate(False)
        self.border_box.place(x = 17, y = 157)

        self.label = ctk.CTkLabel(self, fg_color="black", text="", width=300, height=180)
        self.label.place(x=20, y=160)

        self.end_button = ctk.CTkButton(self, text="End Hunt", font=("Basic", 20), width=110, height=40, command=lambda: end_hunt(), corner_radius=5, border_width=3, border_color="black")
        self.end_button.place(x=345, y=410)


        title_font = ctk.CTkFont(family="Knewave", size=55)

        self.hunting = ctk.CTkLabel(self, text_color="#3d9beb", font=title_font, text=f" Hunting {config.pokemon_name} in {config.game_name} ")
        self.hunting.pack(pady=15)

        config.status="Idle"

        self.status_label = ctk.CTkLabel(self, fg_color="#5e5e5e", anchor="w", width=290, text_color="white", font=("Basic", 29), text=f"Status: {config.status} ")
        self.status_label.place(x=340, y=170)

        self.resets_label = ctk.CTkLabel(self, fg_color="#5e5e5e", anchor="w", width=220, text_color="white", font=("Basic", 25), text=f"Resets: {config.resets} ")
        self.resets_label.place(x=340, y=208)

        self.spent_label = ctk.CTkLabel(self, fg_color="#5e5e5e", anchor="w", width=220, text_color="white", font=("Basic", 20), text=f"Time Spent: {self.convert_seconds(int(config.time_spent))} " )
        self.spent_label.place(x=340, y=240)

        self.time_label = ctk.CTkLabel(self, fg_color="#5e5e5e", anchor="w", width=220, text_color="white", font=("Basic", 20), text=f"Last Reset Time: {config.last_reset_time:.3f} ")
        self.time_label.place(x=340, y=270)

        self.reset_time_label = ctk.CTkLabel(self, fg_color="#5e5e5e", anchor="w", width=220, text_color="white", font=("Basic", 20), text="Average Time/Reset: Loading ")
        self.reset_time_label.place(x=340, y=300)

        self.label.lift()
        self.update_frame()
        self.last_good_frame=time.time()

    def pokemon_names(self, pokemon_name):
        if(pokemon_name=="Registeel"):
            return registeel_commands
        elif(pokemon_name=="Regirock"):
            return regirock_commands
        elif(pokemon_name=="Regice"):
            return regice_commands
        elif(pokemon_name=="Regidrago"):
            return regidrago_commands
        elif(pokemon_name=="Giratina"):
            return giratina_commands
        elif(pokemon_name=="Arceus"):
            return arceus_commands

    def start_controller(self):
         def run():
            config.status="Pairing with Switch"
            self.controller = SwitchController()
            self.controller.connect()
            self.start_time = time.time()
            config.status="Initializing Hunt"
            hm = None
            if(config.game_name=="Sword" or config.game_name=="Shield"):
                hm=sw_sh_hm
            elif(config.game_name=="Brilliant Diamond" or config.game_name=="Shining Pearl"):
                hm=bd_sp_hm
            hunting_manager = hm.HuntingManager(self.controller)
            self.controller.press_home()
            time.sleep(1.5)
            self.controller.press_a()
            time.sleep(1.5)
            config.status="Hunting"
            hunting_manager.run_script(self.pokemon_names(config.pokemon_name))

         threading.Thread(target=run, daemon=True).start()

    def remove_controller(self):
        self.controller.disconnect()

    def start_camera(self):
        if not self.camera_started:
            self.last_good_frame = time.time()
            with config.cap_lock:
                config.cap = cv2.VideoCapture(0)
                opened = config.cap.isOpened()
                if not opened:
                    if config.cap:
                        config.cap.release()
                    config.cap = None
            if not opened:
                config.status = "Failed to Find Capture Card"
                print("[ERROR] Capture card index 0 failed to open.")
                return
            config.status = "Booted up Screen"
            self.camera_started = True

    def stop_camera(self):
        if self.camera_started:
            with config.cap_lock:
                if config.cap:
                    config.cap.release()
                config.cap = None
            self.camera_started = False
            config.start_camera = False
            self.remove_controller()
            self.callback()
        else:
            self.callback()

    def update_frame(self):
        if(self.initialize_time!=self.start_time and config.status!="Shiny Detected!" and config.status != "Ending Hunt"):
            config.time_spent+=(time.time()-self.start_time)
            config.current_reset_time+=(time.time()-self.start_time)
            self.start_time=time.time()

        #Where we update all of the displays
        self.hunting.configure(text=f"Hunting {config.pokemon_name} in {config.game_name} ")
        self.resets_label.configure(text=f"Resets: {config.resets} ")
        self.status_label.configure(text=f"Status: {config.status} ")
        self.spent_label.configure(text=f"Time Spent: {self.convert_seconds(int(config.time_spent))} ")
        self.time_label.configure(text=f"Last Reset Time: {config.last_reset_time:.3f} ")


        if(config.resets!=0):
            self.reset_time_label.configure(text=f"Average Time/Reset: {(config.time_spent-config.current_reset_time)/config.resets:.3f}")
        if config.start_camera and not self.camera_started and not config.egg_hunt:
            self.start_camera()
            if(self.camera_started):
                self.start_controller()
        if self.camera_started:
            self.frame_count+=1
            if self.frame_count % 2 == 0:
                try:
                    ret, frame = False, None
                    with config.cap_lock:
                        cap = config.cap
                        if cap is not None:
                            try:
                                ret, frame = config.cap.read()
                            except cv2.error as e:
                                ret, frame = False, None
                        else:
                            ret, frame = False, None
                    if ret and frame is not None:
                        width = 300
                        height = 180

                        if width > 1 and height > 1:
                            frame = cv2.resize(frame, (width, height))

                        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                        img = Image.fromarray(frame)
                        imgtk = ImageTk.PhotoImage(img)

                        self.label.imgtk = imgtk
                        self.label.configure(image=imgtk)

                    if not ret:
                        if time.time() - self.last_good_frame > 5:
                            print("Capture stalled, reconnecting...")
                            config.status = "Reconnecting Cap Card"
                            with config.cap_lock:
                                if config.cap:
                                    config.cap.release()
                                config.cap = None
                            self.camera_started = False
                            time.sleep(1)
                            self.start_camera()  # this itself locks internally now
                            self.last_good_frame = time.time()
                    else:
                        self.last_good_frame = time.time()

                except cv2.error as e:
                    print(f"Skipping corrupt frame: {e}")


        self.after(16, self.update_frame)

    def release(self):
        with config.cap_lock:
            if config.cap and config.cap.isOpened():
                config.cap.release()

    def convert_seconds(self, total_seconds):
             # Using local variables instead of self.
             days, remainder = divmod(total_seconds, 86400)
             hours, remainder = divmod(remainder, 3600)
             minutes, seconds = divmod(remainder, 60)
             return f"{days:02}:{hours:02}:{minutes:02}:{seconds:02}"