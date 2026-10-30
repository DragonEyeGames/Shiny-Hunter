# Pokémon Shiny Hunter!!!
This is my project that automatically hunts Shiny Pokémon  in Pokémon Sword or Shield! It uses **OpenCV**, **NXBT**, and **CustomTkinter** in order to look at the switch screen, control the switch, and display its results, respectfully.

## Open CV
Open CV is used in order to look at the screen of the switch. My setup uses a cheap capture card off of Amazon plugged into the Switch Dock to accomplish this. To actually detect the shiny, it looks for a menu at a specific time. This menu doesn't pop up until slightly later for a shiny because there is an animation that plays if the Pokémon is shiny.

## NXBT
NXBT is both the savior of the project and the biggest hurdle. It allows the entire system to operate over Bluetooth, making it very simple to get going. This is very convenient, but unfortunately brings a whole host of issues. Many inputs could be dropped, leading to failed runs and wasted time. I was able to fix this by double checking that we made it to a specific screen at the right time. We make sure we made it to the home menu and the game loading screen. With this new system my system works like a charm!

## CustomTkinter
CustomTkinter is the visual component of this whole project. It builds the GUI and allows the user to use the touchscreen to start a hunt. It also looks rather pretty and displays all of the needed information when hunting such as resets and time spent.

## Calibration
This project also has a calibration mode in which you can very easily start hunting. It just goes through a run and records the timings for future use, making it very easy to use the tool.

## Discord Webhook
This project also has a discord webhook so you can see the status of the hunt while on the go! You can get notified when you see a Shiny, and also get logged messages for every reset.

## That's All Folks!
I think that just about sums up my project. I figured that this would be a huge hassle for anyone to setup themselves, so I made a YouTube video to share it with you. Enjoy!
