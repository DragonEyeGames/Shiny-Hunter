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
        super().__init__(parent, bg="#2b2b2b")
        self.callback=back_callback

        self.frame_count = 0
        self.cap = None
        self.camera_started=False

        self.start_time = time.time()
        self.initialize_time = self.start_time

        def end_hunt():
            print("ending hunt")
            config.status="Ending Hunt"
            save_data(config.hunting_data)
            self.stop_camera()

        self.border_box = tk.Frame(self, bg="black", width=788, height=208, relief="groove")
        self.border_box.pack_propagate(False)
        self.border_box.place(x = 6, y = 126)

        self.color_box = tk.Frame(self, bg="#5e5e5e", width=780, height=200, relief="groove")
        self.color_box.pack_propagate(False)
        self.color_box.place(x = 10, y = 130)

        self.border_box = tk.Frame(self, bg="black", width=306, height=186, relief="groove")
        self.border_box.pack_propagate(False)
        self.border_box.place(x = 17, y = 137)

        self.label = tk.Label(self, bg="black")
        self.label.place(x=20, y=140, width=300, height=180)

        self.end_button = tk.Button(self, text="End Hunt", font=("C052", 16), command=lambda: end_hunt())
        self.end_button.place(x=295, y=420, width=110, height=40)

        self.hunting = tk.Label(self, bg="#2b2b2b", fg="white", font=("Droid Sans Fallback", 30), text=f"Hunting {config.pokemon_name} in {config.game_name}")
        self.hunting.pack(pady=35)

        config.status="Idle"

        self.status_label = tk.Label(self, bg="#5e5e5e", fg="white", font=("C052", 20), text=f"Status: {config.status}")
        self.status_label.place(x=340, y=155)

        self.resets_label = tk.Label(self, bg="#5e5e5e", fg="white", font=("C052", 18), text=f"Resets: {config.hunting_data[config.pokemon_name]['resets']}")
        self.resets_label.place(x=340, y=190)

        self.spent_label = tk.Label(self, bg="#5e5e5e", fg="white", font=("C052", 16), text=f"Time Spent: {self.convert_seconds(int(config.hunting_data[config.pokemon_name]['time_spent']))}")
        self.spent_label.place(x=340, y=220)

        self.time_label = tk.Label(self, bg="#5e5e5e", fg="white", font=("C052", 16), text=f"Last Reset Time: {config.last_reset_time:.3f}")
        self.time_label.place(x=340, y=250)

        self.reset_time_label = tk.Label(self, bg="#5e5e5e", fg="white", font=("C052", 16), text="Average Time/Reset: Loading")
        self.reset_time_label.place(x=340, y=280)

        config.hunting_data = load_data(config.hunting_data)
        self.label.lift()
        self.update_frame()

    def start_controller(self):
         def run():
            config.status="Pairing with Switch"
            self.controller = SwitchController()
            self.controller.connect()
            self.start_time = time.time()
            config.status="Initializing Hunt"
            hunting_manager = hm.HuntingManager(self.controller, self.cap)
            self.controller.press_home()
            time.sleep(1.5)
            self.controller.press_a()
            time.sleep(1.5)
            config.status="Hunting"
            hunting_manager.run_script(registeel_commands)

         threading.Thread(target=run, daemon=True).start()

    def remove_controller(self):
        self.controller.disconnect()

    def start_camera(self):
        if not self.camera_started:
            self.cap = cv2.VideoCapture(0)

            #Make sure the card works.
            if not self.cap or not self.cap.isOpened():
                config.status = "Finding Capture Card"
                print("[ERROR] Capture card index 0 failed to open.")
                
                # Clean up the bad object so it doesn't cause loop errors
                if self.cap:
                    self.cap.release()
                self.cap = None
                return  # HALT execution here. Do not start the controller.

            config.status="Booted up Screen"
            self.camera_started=True
            self.start_controller()

    def stop_camera(self):
        if self.camera_started:
            self.cap.release()
            self.cap = None
            self.camera_started=False
            config.start_camera=False
            self.remove_controller()
            self.callback()

    def update_frame(self):
        if(self.initialize_time!=self.start_time and config.status!="Shiny Detected!" and config.status != "Ending Hunt"):
            config.hunting_data[config.pokemon_name]['time_spent']+=(time.time()-self.start_time)
            config.current_reset_time+=(time.time()-self.start_time)
            self.start_time=time.time()
        if(config.pokemon_name not in config.hunting_data):
            config.hunting_data[config.pokemon_name] = 0
        self.hunting.configure(text=f"Hunting {config.pokemon_name} in {config.game_name}")
        self.resets_label.configure(text=f"Resets: {config.hunting_data[config.pokemon_name]['resets']}")
        self.status_label.configure(text=f"Status: {config.status}")
        self.spent_label.configure(text=f"Time Spent: {self.convert_seconds(int(config.hunting_data[config.pokemon_name]['time_spent']))}")
        self.time_label.configure(text=f"Last Reset Time: {config.last_reset_time:.3f}")
        if(config.hunting_data[config.pokemon_name]['resets']!=0):
            self.reset_time_label.configure(text=f"Average Time/Reset: {(config.hunting_data[config.pokemon_name]['time_spent']-config.current_reset_time)/config.hunting_data[config.pokemon_name]['resets']:.3f}")
        if config.start_camera and not self.camera_started:
            self.start_camera()
        if self.camera_started:
            self.frame_count+=1
            if self.frame_count % 2 == 0:
                try:
                    ret, frame = self.cap.read()
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
                except cv2.error as e:
                    print(f"Skipping corrupt frame: {e}")


        self.after(16, self.update_frame)

    def release(self):
        if self.cap and self.cap.isOpened():
            self.cap.release()

    def convert_seconds(self, total_seconds):
             # Using local variables instead of self.
             days, remainder = divmod(total_seconds, 86400)
             hours, remainder = divmod(remainder, 3600)
             minutes, seconds = divmod(remainder, 60)
             return f"{days:02}:{hours:02}:{minutes:02}:{seconds:02}"