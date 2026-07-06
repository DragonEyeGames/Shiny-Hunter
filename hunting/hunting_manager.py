import time
import config
import cv2
import numpy as np
import threading

class HuntingManager:
    def __init__(self, controller, cap):
        self.controller = controller
        self.cap=cap
        self.script = []

    def run_script(self, script):
        self.script=script
        for action, delay in script:
            if(config.status=="Ending Hunt"):
                return
            thread = threading.Thread(target=self.execute, args=(action, delay))
            thread.start()
            time.sleep(delay)

    def execute(self, action, delay, restarting=False):
        if action == "a":
            self.controller.press_a()
        if action == "white_a":
            self.controller.press_a()
            config.status="Loading Encounter"
            detected, ratio, elapsed = self.wait_for_white_flash(self.cap, config.full, timeout=delay-1)
            if detected:
                config.status = "Encounter Loaded"
            else:
                config.status = "No Encounter Detected, Restarting"
                restarting=True
        elif action == "b":
            self.controller.press_b()
        elif action == "left_up":
            self.controller.left_up()
        elif action == "left_left":
            self.controller.left_left()
        elif action == "search":
            config.status="Searching"
            detected, ratio, elapsed = self.wait_for_white_flash(self.cap, config.roi, timeout=0.5)

            if detected:
                config.status="Not Shiny, Restarting"
                restarting=True
            else:
                config.status="Shiny Detected!"

        if(restarting):
            if(config.status=="Ending Hunt"):
                return
            self.controller.press_home()
            time.sleep(2.5)
            if(config.status=="Ending Hunt"):
                return
            config.status="Closing + Rebooting Game"
            self.controller.press_x()
            time.sleep(1.5)
            if(config.status=="Ending Hunt"):
                return
            self.controller.press_a()
            if(config.status=="Ending Hunt"):
                return
            time.sleep(1)

            config.last_reset_time=config.current_reset_time
            config.current_reset_time=0

            config.hunting_data[config.pokemon_name]['resets'] += 1
            self.controller.press_a()
            if(config.status=="Ending Hunt"):
                return
            time.sleep(1)
            self.controller.press_a()
            if(config.status=="Ending Hunt"):
                return
            time.sleep(1)
            self.controller.press_a()
            if(config.status=="Ending Hunt"):
                return
            config.status="Waiting for Game to Load"
            time.sleep(13.5)
            if(config.status=="Ending Hunt"):
                return
            self.controller.press_a()
            time.sleep(3.5)
            if(config.status=="Ending Hunt"):
                return
            config.status="Hunting"
            self.run_script(self.script)

    def get_roi_pixels(self, frame, normalized_roi):
        h, w = frame.shape[:2]
        x = int(normalized_roi["x"] * w)
        y = int(normalized_roi["y"] * h)
        rw = int(normalized_roi["w"] * w)
        rh = int(normalized_roi["h"] * h)
        return x, y, rw, rh

    def is_roi_mostly_white(self, roi_crop, brightness_threshold=240, white_percentage=0.9):
        gray = cv2.cvtColor(roi_crop, cv2.COLOR_BGR2GRAY)
        white_pixels = np.sum(gray >= brightness_threshold)
        total_pixels = gray.size
        ratio = white_pixels / total_pixels
        return ratio >= white_percentage, ratio

    def wait_for_white_flash(self, cap, roi, timeout=0.5, brightness_threshold=240, white_percentage=0.95):
        start_time = time.time()
        last_ratio = 0.0

        while time.time() - start_time < timeout:
            ret, frame = cap.read()
            if not ret:
                continue

            x, y, w, h = self.get_roi_pixels(frame, roi)
            roi_crop = frame[y:y+h, x:x+w]

            is_white, ratio = self.is_roi_mostly_white(roi_crop, brightness_threshold, white_percentage)
            last_ratio = ratio

            if is_white:
                elapsed = time.time() - start_time
                print(f"White flash detected! ({ratio:.2%} white) after {elapsed:.3f}s")
                return True, ratio, elapsed

        elapsed = time.time() - start_time
        print(f"No white flash detected in {elapsed:.3f}s (last ratio: {last_ratio:.2%})")
        return False, last_ratio, elapsed