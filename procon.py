#!/usr/bin/env python3
import os
import threading
import time

input_started = False
report_mode = 0x30

# Reset and open the gadget device
os.system('echo > /sys/kernel/config/usb_gadget/procon/UDC')
os.system('ls /sys/class/udc > /sys/kernel/config/usb_gadget/procon/UDC')
time.sleep(0.5)
gadget = os.open('/dev/hidg0', os.O_RDWR | os.O_NONBLOCK)

counter = 0
mac_addr = '00005e00535e'
initial_input = '81008000f8d77a22c87b0c'

# This is what YOU control from code. Set these True/False to press/release.
buttons = {
    'Y': False, 'X': False, 'B': False, 'A': False,
    'R': False, 'ZR': False,
    'MINUS': False, 'PLUS': False,
    'L': False, 'ZL': False,
    'UP': False, 'DOWN': False, 'LEFT': False, 'RIGHT': False,
}
stick_left = {'x': 0x800, 'y': 0x800}   # center ~0x800 (0-0xFFF range)
stick_right = {'x': 0x800, 'y': 0x800}
handshake_done = threading.Event()

def countup():
    global counter
    while True:
        counter = (counter + 3) % 256
        time.sleep(0.03)

def response(code, cmd, data):
    buf = bytearray([code, cmd])
    buf.extend(data)
    buf.extend(bytearray(64 - len(buf)))
    try:
        os.write(gadget, buf)
    except BlockingIOError:
        pass
    except:
        os._exit(1)

def uart_response(code, subcmd, data):
    buf = bytearray.fromhex(initial_input)
    buf.extend([code, subcmd])
    buf.extend(data)
    response(0x21, counter, buf)

def spi_response(addr, data):
    buf = bytearray(addr)
    buf.extend([0x00, 0x00])
    buf.append(len(data))
    buf.extend(data)
    uart_response(0x90, 0x10, buf)

def pack_stick(x, y):
    return [x & 0xFF, ((x >> 8) & 0xF) | ((y & 0xF) << 4), (y >> 4) & 0xFF]

def input_response():
    while True:
        report = bytearray(11)

        # timer
        report[0] = counter

        # battery + wired
        report[1] = 0x81

        # buttons
        report[2] = (
            (1 if buttons['Y'] else 0) << 0 |
            (1 if buttons['X'] else 0) << 1 |
            (1 if buttons['B'] else 0) << 2 |
            (1 if buttons['A'] else 0) << 3 |
            (1 if buttons['R'] else 0) << 6 |
            (1 if buttons['ZR'] else 0) << 7
        )

        report[3] = (
            (1 if buttons['MINUS'] else 0) << 0 |
            (1 if buttons['PLUS'] else 0) << 1 |
            (1 if buttons['L'] else 0) << 6 |
            (1 if buttons['ZL'] else 0) << 7
        )

        report[4] = (
            (1 if buttons['DOWN'] else 0) << 0 |
            (1 if buttons['UP'] else 0) << 1 |
            (1 if buttons['RIGHT'] else 0) << 2 |
            (1 if buttons['LEFT'] else 0) << 3
        )

        report[5:8] = pack_stick(
            stick_left['x'],
            stick_left['y']
        )

        report[8:11] = pack_stick(
            stick_right['x'],
            stick_right['y']
        )

        print("REPORT:", report.hex())

        response(0x30, counter, report)
        time.sleep(1/60)

def simulate_procon():
    while True:
        try:
            data = os.read(gadget, 128)
            print(f"<<< received: {data.hex()}", flush=True)
            if data[0] == 0x80:
                if data[1] == 0x01:
                    response(0x81, data[1], bytes.fromhex('0003' + mac_addr))
                elif data[1] == 0x02:
                    response(0x81, data[1], [])
                elif data[1] == 0x04:
                    global input_started

                    if not input_started:
                        input_started = True
                        print("Starting input thread")
                        threading.Thread(
                            target=input_response,
                            daemon=True
                        ).start()

                    handshake_done.set()
                elif data[1] == 0x05:
                    response(0x81, data[1], [])
            elif data[0] == 0x01 and len(data) > 16:
                if data[10] == 0x02:
                    uart_response(0x82, data[10], bytes.fromhex('03480302' + mac_addr[::-1] + '0301'))
                elif data[10] in (0x08, 0x30, 0x38, 0x40, 0x48):
                    uart_response(0x80, data[10], [])
                elif data[10] == 0x03:
                    global report_mode
                    report_mode = data[11]
                    print(f"Switch requested report mode {report_mode:02x}")
                    uart_response(0x80, data[10], [])
                elif data[10] == 0x21:
                    uart_response(0xa0, data[10], bytes.fromhex('0100ff0003000501'))
                elif data[10] == 0x10:
                    addr = data[11:13]
                    responses = {
                        b'\x00\x60': 'ffffffffffffffffffffffffffffffff',
                        b'\x50\x60': 'bc114275a928ffffffffffffff',
                        b'\x80\x60': '50fd0000c60f0f30619630f3d41454411554c7799c333663',
                        b'\x98\x60': '0f30619630f3d41454411554c7799c333663',
                        b'\x3d\x60': 'ba156211b87f29065bffe77e0e36569e8560ff323232ffffff',
                        b'\x10\x80': 'ffffffffffffffffffffffffffffffffffffffffffffb2a1',
                        b'\x28\x80': 'beff3e00f001004000400040fefffeff0800e73be73be73b',
                    }
                    if addr in responses:
                        spi_response(addr, bytes.fromhex(responses[addr]))
                    else:
                         print(f"Unknown SPI address requested: {addr.hex()}", flush=True)
        except BlockingIOError:
            pass
        except:
            os._exit(1)

# ============ YOUR MACRO GOES HERE ============
def press(button, duration=0.1):
    print(f"Pressing {button}")
    buttons[button] = True
    time.sleep(duration)
    buttons[button] = False
    print(f"Released {button}")
    time.sleep(0.05)

threading.Thread(target=simulate_procon, daemon=True).start()
threading.Thread(target=countup, daemon=True).start()

print("Waiting for handshake...", flush=True)
handshake_done.wait()   # blocks here until handshake truly finishes, however long that takes
print("Handshake done, sending macro", flush=True)

time.sleep(5)

print("Initializing pushes")

while True:
    press('A', 1)
    time.sleep(1)