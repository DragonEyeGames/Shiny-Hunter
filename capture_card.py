import tkinter as tk
import cv2
from PIL import Image, ImageTk

class CaptureCard(tk.Frame):
    def __init__(self, parent, back_callback):
        super().__init__(parent, bg="black")

        self.label = tk.Label(self)
        self.label.pack()

        self.cap = cv2.VideoCapture(0)

        self.back_button = tk.Button(self, text="Back", command=back_callback)
        self.back_button.pack()

        self.update_frame()

    def update_frame(self):
        ret, frame = self.cap.read()

        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            img = Image.fromarray(frame)
            imgtk = ImageTk.PhotoImage(image=img)

            self.label.imgtk = imgtk
            self.label.configure(image=imgtk)

        self.after(16, self.update_frame)