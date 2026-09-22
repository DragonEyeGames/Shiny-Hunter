# Pokémon Shiny Hunter

A Raspberry Pi-powered Pokémon Shiny Hunter designed to automatically hunt for Shiny Pokémon on the Nintendo Switch and Switch 2!

The Shiny Hunter uses a **Raspberry Pi, capture card, and Bluetooth controller emulation** to control Pokémon games and automatically repeat encounters until a Shiny Pokémon is detected.

---

## Features

* Automatically controls a Nintendo Switch / Switch 2
* Bluetooth controller emulation using **NXBT**
* Uses a capture card to see what is happening on the console
* Automatically detects the appropriate screen/menu states
* Automatically resets the game when a Shiny is not detected
* Built-in touchscreen interface
* Discord Webhook notifications
* Recovery systems for failed inputs and unexpected screens

---

## How It Works

The Shiny Hunter combines several pieces of hardware and software to automate the hunting process.

### 1. Control the Switch

The Raspberry Pi communicates with the Nintendo Switch using **NXBT**, which allows the Pi to emulate a Bluetooth controller.

```text
Raspberry Pi
     │
     │ Bluetooth
     ▼
Nintendo Switch
```

The Shiny Hunter can then send controller inputs to the game automatically.

### 2. See What Is Happening

A capture card sends the Switch's video output to the Raspberry Pi.

The program can analyze the captured video and determine what is currently happening in the game.

```text
Nintendo Switch
      │
      │ HDMI
      ▼
 Capture Card
      │
      │ USB
      ▼
 Raspberry Pi
```

### 3. Detect the Pokémon

The Shiny Hunter navigates to the part of the game where the Pokémon will appear.

It then looks for visual differences in the game's menus and animations that allow it to determine whether the Pokémon is Shiny.

### 4. Repeat

If the Pokémon isn't Shiny, the program automatically resets the game and begins another hunt.

```text
Start Hunt
    │
    ▼
Navigate to Encounter
    │
    ▼
Check Pokémon
    │
 ┌──┴──┐
 │     │
Shiny  Not Shiny
 │     │
 ▼     ▼
Stop  Reset
       │
       └──────► Repeat
```

---

# Reliability & Recovery

One of the biggest challenges with this project has been the reliability of **NXBT**.

Because controller inputs are sent over Bluetooth, inputs can occasionally be dropped or fail to register.

Rather than assuming every input succeeds, the Shiny Hunter uses a series of checks to make sure the game is in the expected state.

If something goes wrong, the program attempts to recover instead of simply getting stuck.

Some of the states it checks include:

* Loading screens
* Pokémon loading
* Home screen
* Game menus
* Expected encounter screens

This allows the Shiny Hunter to continue running for long periods without requiring constant supervision.

---

# Discord Notifications

The Shiny Hunter can connect to Discord using a **Discord Webhook**.

This makes it possible to monitor a hunt remotely.

For example, the Shiny Hunter can notify you when:

* A hunt starts
* A Shiny Pokémon is found
* An error occurs
* The program recovers from an unexpected state

This is especially useful when the Shiny Hunter is running while you're away from it.

```text
Shiny Hunter
     │
     ▼
Discord Webhook
     │
     ▼
   Discord
     │
     ▼
Your Phone / PC
```

---

# Hardware

The Shiny Hunter is built around a Raspberry Pi and a Nintendo Switch.

### Raspberry Pi 4

The **Raspberry Pi 4** is the brains of the entire system.

It handles:

* Controller emulation
* Video processing
* Pokémon detection
* Hunt logic
* The user interface
* Discord notifications

### Capture Card

A USB capture card provides the Raspberry Pi with the Switch's video output.

This allows the program to see and analyze the game.

### 7" Raspberry Pi Display

A 7" Raspberry Pi touchscreen is used to interact with the Shiny Hunter.

From the touchscreen, you can:

* Select a game
* Select a hunt
* Start a hunt
* Monitor progress
* Access hunting features

---

# Software

The project is primarily written in **Python**.

Some of the important technologies used include:

| Technology       | Purpose                              |
| ---------------- | ------------------------------------ |
| Python           | Main application                     |
| CustomTkinter    | User interface                       |
| OpenCV           | Video/capture processing             |
| Pillow           | Image processing                     |
| NXBT             | Nintendo Switch controller emulation |
| Raspberry Pi OS  | Operating system                     |
| Discord Webhooks | Remote notifications                 |

---

# Project Structure

The project is split into several modules so that individual parts of the Shiny Hunter can be developed independently.

```text
Shiny-Hunter/
│
├── main.py
├── config.py
├── capture_card.py
├── switch_controller.py
├── save_manager.py
│
└── ...
```

### `main.py`

The main application and user interface.

### `config.py`

Stores configuration values used throughout the project.

### `capture_card.py`

Handles communication with the capture card and processing of the captured video.

### `switch_controller.py`

Handles communication with the Nintendo Switch through NXBT.

### `save_manager.py`

Handles saving and loading Shiny Hunter data and settings.

---

# Roadmap

There is still plenty left to do!

### Pokémon Support

* [ ] Add more Brilliant Diamond legendary hunts
* [ ] Add Let's Go, Pikachu! support
* [ ] Add Let's Go, Eevee! support
* [ ] Add FireRed support
* [ ] Add LeafGreen support

### Features

* [ ] Improve NXBT reliability
* [ ] Add additional hunting methods
* [ ] Prepare the project for public release

---

# Project

The Shiny Hunter is built to run as a dedicated physical device rather than just a program running on a PC.

The goal is to have a small system that can be connected to a Switch, started from its touchscreen, and then left to hunt while reporting its progress through Discord.

---

# Disclaimer

This project is intended for educational and personal use.

You are responsible for understanding and following the rules and terms of service of any games, consoles, software, or online services you use with this project.

---

# Future

The project isn't finished yet!

There are still a handful of things I want to improve before making the project publicly available. The biggest upcoming goal is expanding support to more Pokémon and hunting methods.

If you want to follow the project, stay tuned for future updates!
