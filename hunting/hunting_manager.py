import time 
import config 
import cv2 
import numpy as np 
import threading 
from save_manager import save_data
from discord_webhook import send_discord_update, send_rich_embed
# Create a custom exception to cleanly break out of nested execution loops
class RestartScriptException(Exception):
    pass

class HuntingManager:
    def __init__(self, controller, cap):
        self.controller = controller
        self.cap = cap
        self.script = []

    def run_script(self, script):
        self.script = script
        #print("Starting script loop...")
        # Use an outer infinite loop so the script can truly reset from the beginning
        while True:
           # print("Loop")
            if config.status == "Ending Hunt":
                return
                
            try:
                for action, delay in self.script:
                    if config.status == "Ending Hunt":
                        return
                        
                    current_time = time.time()
                    #print(f"Executing action '{action}' with delay {delay}s")
                    self.execute(action, delay)
                    #print(f"Executed action '{action}' with delay {delay}s")
                    time_to_wait = delay - (time.time() - current_time)
                    if time_to_wait < 0:
                        time_to_wait = 0
                    time.sleep(time_to_wait)
                    
            except RestartScriptException:
                print("Restarting script loop from the beginning...")
                continue

    def execute(self, action, delay):
        restarting = False
        
        if action == "a":
            #print("Pressing A")
            self.controller.press_a()
            #print("Pressed A")
        elif action == "white_a":
            #print("LOOKING FOR WHITE THINGY")
            self.controller.press_a()
            config.status = "Checking Encounter"
            detected, ratio, elapsed = self.wait_for_white_flash(self.cap, config.full, timeout=delay-1)
            if detected:
                config.status = "Encounter Loaded"
            else:
                config.status = "Encounter Not Loaded" #We didn't find it. So save time, we will try to recover it.
                self.controller.press_a()
                time.sleep(0.1)
                self.controller.press_a()
                time.sleep(0.1)
                self.controller.press_a()
                time.sleep(0.1)
                self.controller.press_a()
                time.sleep(0.1)
                detected, ratio, elapsed = self.wait_for_white_flash(self.cap, config.full, timeout=delay-1)
                if(detected):
                    config.status="Encounter Loaded"
                else:
                    config.status="Restarting Encounter"
                    restarting = True
        elif action == "b":
            self.controller.press_b()
        elif action == "left_up":
            self.controller.left_up()
        elif action == "left_left":
            self.controller.left_left()
        elif action == "search":
            config.hunting_data[config.pokemon_name]['resets'] += 1
            config.last_reset_time = config.current_reset_time
            config.current_reset_time = 0
            save_data(config.hunting_data)
            config.status = "Searching"
            detected, ratio, elapsed = self.wait_for_white_flash(self.cap, config.roi, timeout=0.5)
            if detected:
                config.status = "Not Shiny, Restarting"
                send_discord_update(f"Not Shiny. Currently at {config.hunting_data[config.pokemon_name]['resets']} Resets.")
                restarting = True
            else:
                config.status = "Shiny Detected!"
                send_rich_embed("Shiny Detected!", f"@everyone Shiny Detected in {config.hunting_data[config.pokemon_name]['resets']} Resets!", 14406663)
                while config.status == "Shiny Detected!":
                    time.sleep(1.0) 

        if restarting:
            self.home=False
            while not self.home:
                if config.status == "Ending Hunt": return
                self.controller.press_home()
                if config.status == "Ending Hunt": return
                config.status="Looking for Home"
                detected, ratio, elapsed = self.wait_for_white_flash(self.cap, config.home, timeout=3, brightness_threshold=230, white_percentage = .99)
                if config.status == "Ending Hunt": return
                if(not detected):
                    config.status="Home Not Found"
                    time.sleep(.2)
                else:
                    config.status="Home Found"
                    self.home=True

            time.sleep(.2)
            
            if config.status == "Ending Hunt": return
            config.status = "Rebooting Game"
            self.controller.press_x()
            time.sleep(1.0)
            
            if config.status == "Ending Hunt": return
            self.controller.press_a()
            time.sleep(1.0)
            
            self.controller.press_a()
            time.sleep(0.5)
            self.controller.press_a()
            time.sleep(0.5)
            self.controller.press_a()
            time.sleep(1)
            

            self.load=False
            while not self.load:
                if config.status == "Ending Hunt": return
                self.controller.press_a()
                if config.status == "Ending Hunt": return
                config.status="Finding Loader"
                detected, ratio, elapsed = self.wait_for_black_flash(self.cap, config.load, timeout=3)
                if config.status == "Ending Hunt": return
                if(not detected):
                    config.status="No Loading Screen"
                else:
                    config.status="Loading Screen Found"
                    self.load=True
            time.sleep(1)
            if config.status == "Ending Hunt": return
            config.status="Loading Game"
            time.sleep(9)
            
            if config.status == "Ending Hunt": return
            self.controller.press_a()
            time.sleep(3.5)
            
            config.status = "Starting Encounter"
            
            # Instead of calling self.run_script inside here, raise the exception
            raise RestartScriptException()

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

    def is_roi_mostly_black(self, roi_crop, darkness_threshold=10, black_percentage=0.9):
        gray = cv2.cvtColor(roi_crop, cv2.COLOR_BGR2GRAY)
        black_pixels = np.sum(gray <= darkness_threshold)
        total_pixels = gray.size
        ratio = black_pixels / total_pixels
        return ratio >= black_percentage, ratio

    def wait_for_white_flash(self, cap, roi, timeout=0.5, brightness_threshold=240, white_percentage=0.95):
        start_time = time.time()
        last_ratio = 0.0
        while time.time() - start_time < timeout:
            try:
                ret, frame = cap.read()
            except cv2.error as e:
                # corrupt/truncated JPEG frame from the capture card - skip it, don't crash
                continue

            if not ret or frame is None:
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

    def wait_for_black_flash(self, cap, roi, timeout=0.5, darkness_threshold=10, black_percentage=0.95):
        start_time = time.time()
        last_ratio = 0.0
        while time.time() - start_time < timeout:
            ret, frame = cap.read()
            if not ret:
                continue
            x, y, w, h = self.get_roi_pixels(frame, roi)
            roi_crop = frame[y:y+h, x:x+w]
            is_black, ratio = self.is_roi_mostly_black(roi_crop, darkness_threshold, black_percentage)
            last_ratio = ratio
            if is_black:
                elapsed = time.time() - start_time
                print(f"Black flash detected! ({ratio:.2%} black) after {elapsed:.3f}s")
                return True, ratio, elapsed
        elapsed = time.time() - start_time
        print(f"No white black detected in {elapsed:.3f}s (last ratio: {last_ratio:.2%})")
        return False, last_ratio, elapsed