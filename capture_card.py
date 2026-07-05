import tkinter as tk
import cv2
from PIL import Image, ImageTk
import config
from switch_controller import SwitchController
import threading
import time
from hunting.sw_sh_registeel import commands as registeel_commands
import hunting.hunting_manager as hm
from save_manager import save_data, load_data

class CaptureCard(tk.Frame):
    def __init__(self, parent, back_callback, camera_index=0):
        super().__init__(parent, bg="black")

        self.label = tk.Label(self, bg="black")
        self.label.place(x=10, y=80, width=300, height=180)

        self.cap = None
        self.camera_started=False
        self.back_button = tk.Button(
            self,
            text="Back",
            font=("Arial", 16),
            command=back_callback
        )
        #self.back_button.place(x=690, y=20, width=100, height=40)

        def end_hunt():
            print("ending hunt")
            config.status="Ending Hunt"
            save_data(config.hunting_data)

        self.end_button = tk.Button(self, text="End Hunt", font=("Arial", 16), command=lambda: end_hunt())
        self.end_button.place(x=300, y=350, width=100, height=40)

        self.hunting = tk.Label(self, bg="black", fg="white", font=("Arial", 20), text=f"Hunting {config.pokemon_name} in {config.game_name}")
        self.hunting.place(x=10, y=20)

        config.status="Idle"

        self.status_label = tk.Label(self, bg="black", fg="white", font=("Arial", 20), text=f"Status: {config.status}")
        self.status_label.place(x=330, y=110)

        self.resets_label = tk.Label(self, bg="black", fg="white", font=("Arial", 16), text=f"Resets: {config.hunting_data[config.pokemon_name]["resets"]}")
        self.resets_label.place(x=330, y=140)

        self.spent_label = tk.Label(self, bg="black", fg="white", font=("Arial", 16), text=f"Time Spent: {config.hunting_data[config.pokemon_name]["time_spent"]:.3f}")
        self.spent_label.place(x=330, y=170)

        self.time_label = tk.Label(self, bg="black", fg="white", font=("Arial", 16), text=f"Time Per Reset: {config.last_reset_time:.3f}")
        self.time_label.place(x=330, y=200)

        #config.hunting_data = load_data(config.hunting_data)

        self.update_frame()

    def start_controller(self):
         def run():
            config.status="Pairing with Switch"
            self.controller = SwitchController()
            self.controller.connect()
            config.status="Initializing Hunt"
            hunting_manager = hm.HuntingManager(self.controller, self.cap)
            self.controller.press_home()
            time.sleep(1.5)
            self.controller.press_a()
            time.sleep(1.5)
            config.status="Hunting"
            hunting_manager.run_script(registeel_commands)

         threading.Thread(target=run, daemon=True).start()

    def start_camera(self):
        if not self.camera_started:
            self.cap = cv2.VideoCapture(0)

            #Make sure the card works.
            if not self.cap or not self.cap.isOpened():
                config.status = "Error: Capture Card Not Found!"
                print("[ERROR] Capture card index 0 failed to open.")
                
                # Clean up the bad object so it doesn't cause loop errors
                if self.cap:
                    self.cap.release()
                self.cap = None
                return  # HALT execution here. Do not start the controller.

            config.status="Booted up Screen"
            self.camera_started=True
            self.start_controller()

    def update_frame(self):
        if(config.pokemon_name not in config.hunting_data):
            config.hunting_data[config.pokemon_name] = 0
        self.hunting.configure(text=f"Hunting {config.pokemon_name} in {config.game_name}")
        self.resets_label.configure(text=f"Resets: {config.hunting_data[config.pokemon_name]["resets"]}")
        self.status_label.configure(text=f"Status: {config.status}")
        self.spent_label.configure(text=f"Time Spent: {config.hunting_data[config.pokemon_name]["time_spent"]:.3f}")
        if config.start_camera and not self.camera_started:
            self.start_camera()
        if self.camera_started:
            config.hunting_data[config.pokemon_name]["time_spent"] += 0.016
            config.curret_reset_time += 0.016
            ret, frame = self.cap.read()

            if ret:
                width = 300
                height = 180

                if width > 1 and height > 1:
                    frame = cv2.resize(frame, (width, height))

                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                img = Image.fromarray(frame)
                imgtk = ImageTk.PhotoImage(img)

                self.label.imgtk = imgtk
                self.label.configure(image=imgtk)

        self.after(16, self.update_frame)

    def release(self):
        if self.cap and self.cap.isOpened():
            self.cap.release()