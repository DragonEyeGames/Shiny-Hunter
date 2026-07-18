import tkinter as tk
import cv2
import numpy as np
from PIL import Image, ImageTk
import config
from switch_controller import SwitchController
import threading
import time

from save_manager import save_data, load_data

class MasudaHunt(tk.Frame):
    def __init__(self, parent, back_callback, camera_index=0):
        super().__init__(parent, bg="#2b2b2b")
        self.callback=back_callback

        self.frame_count = 0
        self.camera_started=False

        self.start_time = time.time()
        self.initialize_time = self.start_time

        #The eggs in party
        self.eggs=0

        #The hatched pokemon in party
        #self.pokemon=0

        self.cycles=0

        self.hatched_egg=False

        def end_hunt():
            print("ending hunt")
            config.status="Ending Hunt"
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
        self.end_button.place(x=345, y=420, width=110, height=40)

        self.hunting = tk.Label(self, bg="#2b2b2b", fg="white", font=("Droid Sans Fallback", 30), text=f"Egg Hunting!")
        self.hunting.pack(pady=35)

        config.status="Idle"

        self.status_label = tk.Label(self, bg="#5e5e5e", fg="white", font=("C052", 20), text=f"Status: {config.status}")
        self.status_label.place(x=340, y=155)

        self.resets_label = tk.Label(self, bg="#5e5e5e", fg="white", font=("C052", 18), text=f"Eggs: {self.eggs}")
        self.resets_label.place(x=340, y=190)

        self.spent_label = tk.Label(self, bg="#5e5e5e", fg="white", font=("C052", 16), text=f"Time Spent: {self.convert_seconds(int(config.hunting_data[config.pokemon_name][config.game_name]['time_spent']))}")
        self.spent_label.place(x=340, y=220)

        self.reset_time_label = tk.Label(self, bg="#5e5e5e", fg="white", font=("C052", 16), text="Average Time/Egg: Loading")
        self.reset_time_label.place(x=340, y=280)

        config.hunting_data = load_data(config.hunting_data)

        self.label.lift()
        self.update_frame()
        self.last_good_frame=time.time()

    def start_controller(self):
         def run():
            config.status="Pairing with Switch"
            self.controller = SwitchController()
            self.controller.connect()
            self.start_time = time.time()
            config.status="Initializing Hunt"
            self.initialize_time=time.time()

            while True:
                print(self.shiny_egg())
                """time.sleep(1.5)
                config.status="Going Down"
                self.controller.left_down(.5)
                time.sleep(.1)
                config.status="Boarding Bike"
                self.controller.left_right(.1)
                time.sleep(.1)
                self.controller.press_plus()
                time.sleep(.5)
                config.status="Going Right"
                for _ in range(18):
                    self.controller.left_right(1)
                    self.egg_check()
                config.status="Swapping Bike"
                time.sleep(.1)
                self.egg_check()
                self.controller.press_plus()
                time.sleep(1)
                self.controller.left_left()
                time.sleep(.1)
                self.egg_check()
                self.controller.press_plus()
                time.sleep(.5)
                self.egg_check()
                config.status="Going Left"
                for _ in range(19):
                    self.controller.left_left(1)
                    self.egg_check()
                config.status="Going Up"
                self.controller.press_plus()
                self.egg_check()
                time.sleep(1)
                self.egg_check()
                self.controller.left_up(1)
                self.egg_check()
                for _ in range(5):
                    self.controller.left_diagonal_right(1)
                    self.egg_check()
                if(self.eggs<5):
                    self.get_egg()"""

         def check_for_egg():
             while True:
                 time.sleep(.5)
                 ret, frame = False, None
                 with config.cap_lock:
                    cap = config.cap
                    if cap is not None:
                        try:
                            ret, frame = cap.read()
                        except cv2.error:
                            ret, frame = False, None
                 if ret and frame is not None:
                    egg=self.check_gray(frame, config.sw_sh_egg)
                    if(egg and self.hatched_egg==False):
                        self.hatched_egg=True
                 #print(self.hatched_egg)


         threading.Thread(target=run, daemon=True).start()
         #threading.Thread(target=check_for_egg, daemon=True).start()

    def hatch_egg(self):
        config.status="Hatching Egg"
        time.sleep(.1)
        self.controller.press_a()
        time.sleep(15)
        self.controller.press_a()
        time.sleep(5)
        self.controller.press_b()
        time.sleep(1)
        self.check_shiny()
        self.hatched_egg=False
        self.eggs-=1

    def check_shiny(self):
        #Open up the boxes
        time.sleep(.5)
        self.controller.press_x()
        time.sleep(.5)
        self.controller.press_a()
        time.sleep(1.5)
        self.controller.press_r()
        time.sleep(3.5)
        #View the pokemon we want
        self.controller.press_left()
        time.sleep(.2)
        self.controller.press_down()
        time.sleep(.2)
        #Kill it if non-shiny

        if(self.shiny_egg()):
            self.controller.press_a()
            time.sleep(.2)
            self.controller.press_up()
            time.sleep(.1)
            self.controller.press_up()
            time.sleep(.1)
            self.controller.press_a()
            time.sleep(1)
            self.controller.press_up()
            time.sleep(.1)
            self.controller.press_a()
            time.sleep(2)
            self.controller.press_a()
            time.sleep(1)
            #Exit boxes
            self.controller.press_b()
            time.sleep(3)
            self.controller.press_b()
            time.sleep(2)
            self.controller.press_b()
            time.sleep(1)
        else:
            config.status="Shiny found!"
            while True:
                time.sleep(1)

    def egg_check(self):
        if self.hatched_egg:
            self.hatch_egg()


    def get_egg(self):
        config.status="Acquiring Egg"
        print("Getting egg")
        self.controller.press_a()
        time.sleep(.8)
        self.controller.press_a()
        time.sleep(3)
        self.controller.press_a()
        time.sleep(1.5)
        self.controller.press_a()
        time.sleep(2)
        self.controller.press_a()
        time.sleep(.5)
        self.eggs+=1
        print("Egg Acquired")

    def shiny_egg(self):
         with config.cap_lock:
            cap = config.cap
            if cap is not None:
                try:
                    ret, frame = cap.read()
                except cv2.error:
                    ret, frame = False, None
            if ret and frame is not None:
                #egg=self.check_gray(frame)
                h, w = frame.shape[:2]

                x = int(config.shiny_egg['x'] * w)
                y = int(config.shiny_egg['y'] * h)
                rw = int(config.shiny_egg['w'] * w)
                rh = int(config.shiny_egg['h'] * h)

                region = frame[y:y+rh, x:x+rw]

                lower = np.array([191, 191, 191], dtype=np.uint8)
                upper = np.array([255, 255, 255], dtype=np.uint8)

                mask = cv2.inRange(region, lower, upper)

                fill = cv2.countNonZero(mask) / (rw * rh)
                print(fill)
                return fill >= 0.90

    def check_gray(self, frame, roi):
        h, w = frame.shape[:2]

        x = int(roi['x'] * w)
        y = int(roi['y'] * h)
        rw = int(roi['w'] * w)
        rh = int(roi['h'] * h)

        region = frame[y:y+rh, x:x+rw]

        lower = np.array([44, 44, 44], dtype=np.uint8)
        upper = np.array([52, 52, 52], dtype=np.uint8)

        mask = cv2.inRange(region, lower, upper)

        fill = cv2.countNonZero(mask) / (rw * rh)

        return fill >= 0.90



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
                config.status = "Finding Capture Card"
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

    def update_frame(self):

        #Update the UI stuff
        self.resets_label.configure(text=f"Eggs: {self.eggs}")
        self.status_label.configure(text=f"Status: {config.status}")
        self.spent_label.configure(text=f"Time Spent: {self.convert_seconds(int(time.time()-self.initialize_time))}")

        if(config.hunting_data[config.pokemon_name][config.game_name]['resets']!=0):
            if(self.eggs>0):
                self.reset_time_label.configure(text=f"Average Time/Egg: {(time.time()-self.initialize_time())/self.eggs:.3f}")

        #Starting the Camera
        if config.start_camera and not self.camera_started and config.egg_hunt:
            self.start_camera()
            self.start_controller()

        #Displaying the picture
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