import tkinter as tk
import cv2
from PIL import Image, ImageTk


class CaptureCard(tk.Frame):
    def __init__(self, parent, back_callback, camera_index=0):
        super().__init__(parent, bg="black")

        # Video display label
        self.label = tk.Label(self, bg="black")
        self.label.place(x=0, y=0, relwidth=1, relheight=1)

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

        self.update_frame()

    def update_frame(self):
        if self.cap.isOpened():
            ret, frame = self.cap.read()

            if ret:
                # Get the current size of this frame
                width = self.winfo_width()
                height = self.winfo_height()

                # Avoid resizing to 1x1 before Tkinter finishes drawing
                if width > 1 and height > 1:
                    frame = cv2.resize(frame, (width, height))

                # Convert BGR -> RGB
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                # Convert to Tkinter image
                img = Image.fromarray(frame)
                imgtk = ImageTk.PhotoImage(img)

                self.label.imgtk = imgtk
                self.label.configure(image=imgtk)

        # Update again in ~16 ms (~60 FPS)
        self.after(16, self.update_frame)

    def release(self):
        if self.cap.isOpened():
            self.cap.release()