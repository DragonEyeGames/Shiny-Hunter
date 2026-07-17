import threading

pokemon_name="(loading)"
game_name="(loading)"
start_camera=False

status="Idle"

hunting_data = {
    "Registeel": {
        "Sword": {
            "resets": 0,
            "time_spent": 0.000
        },
        "Shield": {
            "resets": 0,
            "time_spent": 0.000
        },
        "Brilliant Diamond": {
            "resets": 0,
            "time_spent": 0.000
        },
        "Shining Pearl": {
            "resets": 0,
            "time_spent": 0.000
        }
    },
    "Regirock": {
        "Sword": {
            "resets": 0,
            "time_spent": 0.000
        },
        "Shield": {
            "resets": 0,
            "time_spent": 0.000
        },
        "Brilliant Diamond": {
            "resets": 0,
            "time_spent": 0.000
        },
        "Shining Pearl": {
            "resets": 0,
            "time_spent": 0.000
        }
    },
    "Regice": {
        "Sword": {
            "resets": 0,
            "time_spent": 0.000
        },
        "Shield": {
            "resets": 0,
            "time_spent": 0.000
        },
        "Brilliant Diamond": {
            "resets": 0,
            "time_spent": 0.000
        },
        "Shining Pearl": {
            "resets": 0,
            "time_spent": 0.000
        }
    },
    "Regidrago": {
        "Sword": {
            "resets": 0,
            "time_spent": 0.000
        },
        "Shield": {
            "resets": 0,
            "time_spent": 0.000
        }
    },
    #"Regieleki": {
     #   "Sword": {
      #      "resets": 0,
       #     "time_spent": 0.000
       # },
       # "Shield": {
       #     "resets": 0,
       #     "time_spent": 0.000
       # }
    #},
    "Giratina": {
        "Brilliant Diamond": {
            "resets": 0,
            "time_spent": 0.000
        },
        "Shining Pearl": {
            "resets": 0,
            "time_spent": 0.000
        }
    },
    "Arceus": {
        "Brilliant Diamond": {
            "resets": 0,
            "time_spent": 0.000
        },
        "Shining Pearl": {
            "resets": 0,
            "time_spent": 0.000
        }
    },
    "(loading)": {
        "(loading)": {
            "resets": 0,
            "time_spent": 0.000
        }
    }
}



current_reset_time=0.000
last_reset_time=0.000

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

game_screen = {'x': 0.0765625, 'y': 0.2604166666666667, 'w': 0.2171875, 'h': 0.38125}

bd_sp_menu = {'x': 0.870, 'y': 0.583, 'w': 0.05, 'h': 0.0667}

egg_hunt = False