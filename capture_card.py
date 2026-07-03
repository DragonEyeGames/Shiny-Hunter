import tkinter as tk
import cv2
from PIL import Image, ImageTk
import config

class CaptureCard(tk.Frame):
    def __init__(self, parent, back_callback, camera_index=0):
        super().__init__(parent, bg="black")

        # Video display label
        self.label = tk.Label(self, bg="black")
        self.label.place(x=0, y=200, relwidth=1, relheight=1)

        # Open the camera/capture card
        self.cap = cv2.VideoCapture(camera_index)

        if not self.cap.isOpened():
            print(f"Could not open camera {camera_index}")

        # Back button (placed over the video)
        self.back_button = tk.Button(
            self,
            text="Back",
            font=("Arial", 16),
            command=back_callback
        )
        self.back_button.place(x=10, y=10, width=100, height=40)

        self.hunting = tk.Label(self, bg="black", fg="white", font=("Arial", 16), text=f"Hunting {config.pokemon_name}")

        self.update_frame()

    def update_frame(self):
        if self.cap.isOpened():
            ret, frame = self.cap.read()

            if ret:
                width = 200
                height = 120

                if width > 1 and height > 1:
                    frame = cv2.resize(frame, (width, height))

                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                img = Image.fromarray(frame)
                imgtk = ImageTk.PhotoImage(img)

                self.label.imgtk = imgtk
                self.label.configure(image=imgtk)

        self.after(16, self.update_frame)

    def release(self):
        if self.cap.isOpened():
            self.cap.release()