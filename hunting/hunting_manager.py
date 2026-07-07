import time 
import config 
import cv2 
import numpy as np 
import threading 
from save_manager import save_data
from discord_webhook import send_discord_update, send_shiny_notification
from datetime import datetime

# Create a custom exception to cleanly break out of nested execution loops
class RestartScriptException(Exception):
    pass

class HuntingManager:
    def __init__(self, controller, cap):
        self.controller = controller
        self.cap = cap
        self.script = []
        self.frame_count=0

    def run_script(self, script): 
        self.script = script 
        
        while True: 
            if config.status == "Ending Hunt": 
                return 
            try: 
                for action, delay in self.script: 
                    if config.status == "Ending Hunt": 
                        return 
                    current_time = time.time() 
                    self.execute(action, delay) 
                    
                    time_to_wait = delay - (time.time() - current_time) 
                    if time_to_wait < 0: 
                        time_to_wait = 0 
                    time.sleep(time_to_wait) 
            except RestartScriptException: 
                print("Restarting script loop from the beginning...") 
                continue 

    def execute(self, action, delay): 
        if action == "a": 
            self.controller.press_a() 
            
        elif action == "white_a": 
            self.controller.press_a() 
            config.status = "Checking Encounter" 
            detected, ratio, elapsed = self.wait_for_white_flash(self.cap, config.full, timeout=delay-1) 
            
            if detected: 
                config.status = "Encounter Loaded" 
            else: #I attempted adding in recovery steps, but the timings would be too innacurate. This is the way
               self.trigger_soft_reset() 
               raise RestartScriptException() 

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
            
            detected, ratio, elapsed = self.wait_for_white_flash(self.cap, config.roi, timeout=0.8) 
            if detected: 
                config.status = "Not Shiny, Restarting" 
                military_time = datetime.now().strftime("%H:%M") 
                send_discord_update(f"Not Shiny. Currently at {config.hunting_data[config.pokemon_name]['resets']} Resets. Timestamp: {military_time}.") 
                #Restart the script
                self.trigger_soft_reset()
                raise RestartScriptException() 
            else: 
                config.status = "Shiny Detected!" 
                military_time = datetime.now().strftime("%H:%M") 
                send_shiny_notification("Shiny Detected!", f"@everyone Shiny Detected in {config.hunting_data[config.pokemon_name]['resets']} Resets! Timestamp: {military_time}.", 14406663) 
                while config.status == "Shiny Detected!": 
                    time.sleep(1.0) 
                if(config.status== "False Positive"):
                    self.trigger_soft_reset()
                    raise RestartScriptException() 

    def find_home(self):
        self.home = False 
        while not self.home: 
            if config.status == "Ending Hunt": return 
            self.controller.press_home() 
            if config.status == "Ending Hunt": return 
            config.status = "Looking for Home" 
            detected, ratio, elapsed = self.wait_for_white_flash(self.cap, config.home, timeout=3, brightness_threshold=230, white_percentage=.99) 
            if config.status == "Ending Hunt": return 
            if not detected: 
                config.status = "Home Not Found" 
                time.sleep(.2) 
            else: 
                config.status = "Home Found" 
                self.home = True 
                time.sleep(.2) 

    def find_loader(self):
        self.load = False 
        attempts=0
        while not self.load and attempts<3: 
            if config.status == "Ending Hunt": return 
            self.controller.press_a() 
            if config.status == "Ending Hunt": return 
            config.status = "Finding Loader" 
            detected, ratio, elapsed = self.wait_for_black_flash(self.cap, config.load, timeout=3) 
            if config.status == "Ending Hunt": return 
            if not detected: 
                config.status = "No Loading Screen" 
            else: 
                config.status = "Loading Screen Found" 
                self.load = True 
            attempts+=1
            time.sleep(1)
        if attempts>=3: #Couldn't find load menu in reasonable time
            self.find_home() #Assume we didn't make it home
            self.reboot_game() # Kill the game
            self.find_loader() #Try to find home again

    def reboot_game(self):
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

    def trigger_soft_reset(self):

        self.find_home()
                
        self.reboot_game()
        
        self.find_loader()
            
        if config.status == "Ending Hunt": return 
        config.status = "Loading Game" 
        time.sleep(9) 
        if config.status == "Ending Hunt": return 
        self.controller.press_a() 
        time.sleep(3.5) 
        config.status = "Starting Encounter"

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
            self.frame_count+=1
            if self.frame_count % 2 != 0:
                continue #Skipping every other frame to save resources
            try:
                ret, frame = cap.read()
            except cv2.error as e:
                print("Skipping corrupt frame")
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
            self.frame_count+=1
            if self.frame_count % 2 != 0:
                continue #Skipping every other frame to save resources
            try:
                ret, frame = cap.read()
            except cv2.error as e:
                print("Skipping corrupt frame")
                continue

            if not ret or frame is None:
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