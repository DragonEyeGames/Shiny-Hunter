from nxbt import Nxbt
import time


class SwitchController:
    def __init__(self):
        self.nx = Nxbt()
        self.controller_index = None
        self.connected = False

    # -------------------------
    # CONNECT CONTROLLER
    # -------------------------
    def connect(self):
        if self.connected:
            print("Already connected.")
            return

        print("Creating controller...")

        self.controller_index = self.nx.create_controller(
            self.nx.PRO_CONTROLLER
        )

        print("Put Switch in 'Change Grip/Order' screen now...")

        self.nx.wait_for_connection(self.controller_index)

        self.connected = True
        print("Controller connected!")

    # -------------------------
    # PRESS ANY BUTTON
    # -------------------------
    def press_button(self, button, hold_time=0.05):
        if not self.connected or self.controller_index is None:
            print("Controller not connected!")
            return

        self.nx.press_buttons(self.controller_index, [button])
        time.sleep(hold_time)
        self.nx.release_buttons(self.controller_index, [button])

    # -------------------------
    # CONVENIENCE FUNCTIONS
    # -------------------------
    def press_a(self):
        self.press_button("A")

    def press_b(self):
        self.press_button("B")

    def press_home(self):
        self.press_button("HOME")

    def press_start(self):
        self.press_button("PLUS")

    # -------------------------
    # CLEANUP
    # -------------------------
    def disconnect(self):
        if self.controller_index is not None:
            print("Stopping controller...")
            self.nx.stop_controller(self.controller_index)
            self.connected = False
            self.controller_index = None