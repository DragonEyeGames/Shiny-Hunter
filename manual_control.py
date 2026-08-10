import tkinter as tk
import cv2
from PIL import Image, ImageTk
import config
from switch_controller import SwitchController
import threading
import time
import numpy as np

class ManualControl(tk.Frame):
    def __init__(self, parent, back_callback, camera_index=0):
        super().__init__(parent, bg="#2b2b2b")
        self.callback=back_callback

        self.frame_count = 0
        self.camera_started=False

        self.label = tk.Label(self, bg="black")
        self.label.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.update_frame()
        self.last_good_frame=time.time()

    def start_controller(self):
         def run():
            config.status="Pairing with Switch"
            self.controller = SwitchController()
            self.controller.connect()

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
        if config.start_camera and not self.camera_started:
            self.start_camera()
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
                        label_w = self.label.winfo_width()
                        label_h = self.label.winfo_height()

                        if label_w > 1 and label_h > 1:
                            frame_h, frame_w = frame.shape[:2]

                            # Scale factor that fits the frame inside the label without distortion
                            scale = min(label_w / frame_w, label_h / frame_h)
                            new_w = max(1, int(frame_w * scale))
                            new_h = max(1, int(frame_h * scale))

                            resized = cv2.resize(frame, (new_w, new_h))

                            # Create a black canvas the size of the label, then center the resized frame on it
                            canvas = np.zeros((label_h, label_w, 3), dtype=np.uint8)
                            x_offset = (label_w - new_w) // 2
                            y_offset = (label_h - new_h) // 2
                            canvas[y_offset:y_offset+new_h, x_offset:x_offset+new_w] = resized

                            frame = canvas

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