import time
import nxbt

def test_background_reconnect():
    nx = nxbt.Nxbt()
    print("Initializing testing controller...")
    
    index = nx.create_controller(nxbt.PRO_CONTROLLER)

    nx.wait_for_connection(index)
    
    time.sleep(2)
    
    nx.press_buttons(index, [nxbt.Buttons.DPAD_DOWN])
    time.sleep(2)
    
    nx.disconnect(index)
    
    time.sleep(3)
    
    print("!!! ATTEMPTING BACKGROUND RECONNECT !!!")
    nx.connect(index)
    
    time.sleep(3)

    print("Testing post-reconnect input: Pressing UP...")
    nx.press_buttons(index, [nxbt.Buttons.DPAD_UP])
    time.sleep(2)
    
    print("Test complete. If the cursor moved UP, background recovery works!")

if __name__ == "__main__":
    test_background_reconnect()