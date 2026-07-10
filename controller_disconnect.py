from switch_controller import SwitchController
import time

sc = SwitchController()
sc.connect()
print("Connected. Cached address:", sc.switch_address)
print("Initial state:", sc.nx.state[sc.controller_index])

input("Press Enter to simulate a dead connection and trigger reconnect()...")

sc.connected = False
success = sc.reconnect()
print("Reconnect result:", success)

if success:
    print("Post-reconnect state:", sc.nx.state[sc.controller_index])
    time.sleep(2)
    print("State after 2s settle:", sc.nx.state[sc.controller_index])

    result = sc.press_a()
    print("press_a() return value:", result)
    print("Final state:", sc.nx.state[sc.controller_index])