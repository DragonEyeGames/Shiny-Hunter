import threading

pokemon_name=""
game_name=""
start_camera=False

status="Idle"

current_reset_time=0.000
last_reset_time=0.000
time_spent=0.000

resets=0

cap = None
cap_lock = threading.Lock()

roi = {
    "x": 0.8703125,
    "y": 0.7861,
    "w": 0.04739583,
    "h": 0.083,
}

full = {
    "x": 0.0,
    "y": 0.0,
    "w": 1.0,
    "h": 1.0
    }

home = {
    "x": 0.305,
    "y": 0.178,
    "w": 0.690,
    "h": 0.078
    }

load = {
    "x": 0.0,
    "y":0.707,
    "w": 1.0,
    "h": 0.285
    }

sw_sh_egg = {'x': 0.284375, 'y': 0.8157407407407408, 'w': 0.39114583333333336, 'h': 0.15092592592592594}

shiny_egg = {'x': 0.9692708333333333, 'y': 0.14629629629629629, 'w': 0.022916666666666665, 'h': 0.03981481481481482}


game_screen = {'x': 0.0765625, 'y': 0.2604166666666667, 'w': 0.2171875, 'h': 0.38125}

bd_sp_menu = {'x': 0.870, 'y': 0.583, 'w': 0.05, 'h': 0.0667}

egg_hunt = False