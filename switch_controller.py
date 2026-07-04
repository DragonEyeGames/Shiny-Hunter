from nxbt import Nxbt, PRO_CONTROLLER, Buttons, Sticks
import time

class SwitchController:
    def __init__(self):
        self.nx = Nxbt()
        self.controller_index = None
        self.connected = False

    def connect(self):
        if self.connected:
            print("Already connected.")
            return
        print("Creating controller...")
        self.controller_index = self.nx.create_controller(PRO_CONTROLLER)
        print("Put Switch in 'Change Grip/Order' screen now...")
        self.nx.wait_for_connection(self.controller_index)
        self.connected = True
        print("Controller connected!")

    def press_button(self, button, hold_time=0.05):
        if not self.connected or self.controller_index is None:
            print("Controller not connected!")
            return
        # press_buttons presses AND releases automatically
        self.nx.press_buttons(self.controller_index, [button], down=hold_time)


    def press_a(self):
        self.press_button(Buttons.A)

    def press_b(self):
        self.press_button(Buttons.B)

    def press_x(self):
        self.press_button(Buttons.X)

    def press_y(self):
        self.press_button(Buttons.Y)

    def press_home(self):
        self.press_button(Buttons.HOME)

    def tilt_stick(self, stick, x, y, hold_time=0.05):
        if not self.connected or self.controller_index is None:
            print("Controller not connected!")
            return
        self.nx.tilt_stick(self.controller_index, stick, x, y, tilted=hold_time)

    def left_up(self):
        self.tilt_stick(Sticks.LEFT_STICK, 0, 100)

    def left_left(self):
        self.tilt_stick(Sticks.LEFT_STICK, -100, 0)

    def disconnect(self):
        if self.controller_index is not None:
            print("Stopping controller...")
            self.nx.remove_controller(self.controller_index)
            self.connected = False
            self.controller_index = None