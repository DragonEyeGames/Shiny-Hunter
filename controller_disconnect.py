from switch_controller import SwitchController
import time

sc = SwitchController()
sc.connect()

print("Connected. Cached address:", sc.switch_address)
input("Press Enter to simulate a dead connection and trigger reconnect()...")

# Simulate what press_button sees after repeated timeouts
sc.connected = False

success = sc.reconnect()
print("Reconnect result:", success)

if success:
    sc.press_a()
    print("Sent a test press after reconnecting.")