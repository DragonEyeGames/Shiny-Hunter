import tkinter as tk
import cv2
from PIL import Image, ImageTk

class CaptureCard:
    def __init__(self, root):
        self.root = root

        self.label = tk.Label(root)
        self.label.pack()
        
        self.cap = cv2.VideoCapture(0)

        self.update_frame()

    def update_frame(self):
        ret, frame = self.cap.read()

        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            img = Image.fromarray(frame)
            imgtk = ImageTk.PhotoImage(image=img)

            self.label.imgtk = imgtk
            self.label.configure(image=imgtk)

        self.root.after(16, self.update_frame)


root = tk.Tk()
app = VideoApp(root)
root.mainloop()