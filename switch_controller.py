from nxbt import Nxbt, PRO_CONTROLLER, Buttons, Sticks
import time
import concurrent.futures
import config
from discord_webhook import send_failure_notification
from save_manager import save_address, load_address

class SwitchController:
    def __init__(self):
        self.nx = Nxbt()
        self.controller_index = None
        self.connected = False
        self.switch_address = load_address(None)#None  # cached MAC of the paired Switch, once known

    def connect(self, timeout=60):
        if(self.switch_address!=None):
            if(self.reconnect()):
                return True
        """Initial connect. Requires the Switch to be on the
        'Change Grip/Order' screen the first time you ever pair
        with this host machine."""
        if self.connected:
            print("Already connected.")
            return True

        print("Creating controller...")
        self.controller_index = self.nx.create_controller(PRO_CONTROLLER)
        print("Put Switch in 'Change Grip/Order' screen now...")

        try:
            self.nx.wait_for_connection(self.controller_index)
        except Exception as e:
            print(f"Failed to connect: {e}")
            self.connected = False
            return False

        self.connected = True
        print("Controller connected!")

        # Cache the Switch's address so future reconnects skip the menu
        try:
            addrs = self.nx.get_switch_addresses()
            if addrs:
                self.switch_address = addrs[0]
                save_address(self.switch_address)
        except Exception as e:
            print(f"Could not cache switch address: {e}")

        return True

    def reconnect(self, timeout=60, attempts=3):
        """Recover a dead connection without needing the Switch menu,
        by reconnecting to the cached MAC address. Falls back to a
        fresh connect() (which needs the menu) if no address is cached
        or all reconnect attempts fail."""
        print("Attempting to reconnect...")

        # Tear down the old controller if it still exists
        if self.controller_index is not None:
            try:
                self.nx.remove_controller(self.controller_index)
            except Exception as e:
                print(f"Error removing stale controller: {e}")

        self.controller_index = None
        self.connected = False

        if self.switch_address is None:
            print("No cached Switch address, falling back to full connect() "
                  "(menu required).")
            return self.connect(timeout=timeout)

        for attempt in range(1, attempts + 1):
            print(f"Reconnect attempt {attempt}/{attempts}...")
            try:
                self.controller_index = self.nx.create_controller(
                    PRO_CONTROLLER,
                    reconnect_address=[self.switch_address]
                )
                self.nx.wait_for_connection(self.controller_index)
                self.connected = True
                print("Reconnected successfully!")
                return True
            except Exception as e:
                print(f"Reconnect attempt {attempt} failed: {e}")
                if self.controller_index is not None:
                    try:
                        self.nx.remove_controller(self.controller_index)
                    except Exception:
                        pass
                    self.controller_index = None
                time.sleep(5)

        print("All reconnect attempts failed.")
        self.connected = False
        return False

    def press_button(self, button, hold_time=0.05, timeout=1, max_retries=2):
        if not self.connected or self.controller_index is None:
            print("Controller not connected!")
            return False

        executor = concurrent.futures.ThreadPoolExecutor(max_workers=1)
        try:
            for attempt in range(1, max_retries + 1):
                future = executor.submit(
                    self.nx.press_buttons,
                    self.controller_index,
                    [button],
                    down=hold_time
                )
                try:
                    future.result(timeout=timeout)
                    return True
                except concurrent.futures.TimeoutError:
                    print(f"Timed out after {timeout}s, retrying...")
                    # Don't wait for the stuck thread.
                    executor.shutdown(wait=False, cancel_futures=True)
                    # Start a fresh worker for the next attempt.
                    executor = concurrent.futures.ThreadPoolExecutor(max_workers=1)

            print(f"Failed to press {button} after {max_retries} attempts")
            config.status = "Attempting Reconnect"

            if self.reconnect():
                config.status = "Hunting"
                print("Recovered from failure, resuming hunt.")
                return False  # caller decides whether to retry the press
            else:
                config.status = "Ending Hunt"
                send_failure_notification(
                    "Help Needed!",
                    "Failed to Push Buttons! NXBT Controller Restart Required!",
                    13701636
                )
                return False
        finally:
            executor.shutdown(wait=False, cancel_futures=True)

    def press_a(self):
        return self.press_button(Buttons.A)

    def press_b(self):
        self.press_button(Buttons.B)

    def press_x(self):
        self.press_button(Buttons.X)

    def press_y(self):
        self.press_button(Buttons.Y)

    def press_up(self):
        self.press_button(Buttons.DPAD_UP)

    def press_home(self):
        self.press_button(Buttons.HOME)

    def press_plus(self):
        self.press_button(Buttons.PLUS)

    def press_l(self):
        self.press_button(Buttons.L)

    def tilt_stick(self, stick, x, y, hold_time=0.05):
        if not self.connected or self.controller_index is None:
            print("Controller not connected!")
            return
        self.nx.tilt_stick(self.controller_index, stick, x, y, tilted=hold_time)

    def left_up(self, hold_time=0.05):
        self.tilt_stick(Sticks.LEFT_STICK, 0, 100, hold_time)

    def left_down(self, hold_time=0.05):
        self.tilt_stick(Sticks.LEFT_STICK, 0, -100, hold_time)

    def right_down(self, hold_time=0.05):
        self.tilt_stick(Sticks.RIGHT_STICK, 0, -100, hold_time)

    def left_left(self, hold_time=0.05):
        self.tilt_stick(Sticks.LEFT_STICK, -100, 0, hold_time)

    def left_diagonal_left(self, hold_time=0.05):
        self.tilt_stick(Sticks.LEFT_STICK, -50, 50, hold_time)

    def left_diagonal_left(self, hold_time=0.05):
        self.tilt_stick(Sticks.LEFT_STICK, 50, 50, hold_time)

    def left_right(self, hold_time=0.05):
        self.tilt_stick(Sticks.LEFT_STICK, 100, 0, hold_time)


    def disconnect(self):
        if self.controller_index is not None:
            print("Stopping controller...")
            self.nx.remove_controller(self.controller_index)
            self.connected = False
            self.controller_index = None