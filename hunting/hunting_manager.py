import time

class HuntingManager:
    def __init__(self, controller):
        self.controller = controller

    def run_script(self, script):
        for action, delay in script:
            self.execute(action)
            time.sleep(delay)

    def execute(self, action):
        if action == "a":
            self.controller.press_a()
        elif action == "b":
            self.controller.press_b()
        elif action == "left_up":
            self.controller.left_up()
        elif action == "left_left":
            self.controller.left_left()
        elif action == "search":
            pass