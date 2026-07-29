!Tavern NSFW builder for [GAME]  

`Version 0.1`

Tavern NSFW builder is a python script made for the game [game](link). 

It designed to make 100% safe files (**excluding achivments**) in theoreticly every version of the game (even in the future ones! ... \*hopefuly\*).

# How does it work?

It based on OCR (Optical Character Recognition) and base pyautogui as well as pynput to imulate users inputs. This script abuses the "progress" page on the main menu so it can "scan" the "unseen events" section using OCR to then add them into safe file. Since it grabs the event´s name directly from the game, it can also work on a new version of the game even for events noone had seen before, as long as OCR correctly recognises events names (or it gets corectly corrected by two mistakes checkers). 

# Safe file

In my testing I used my own script to make from 0% to 100% safe file. So if you just need a 100% safe file (not every achivment is unlocked) for version 0.3.69, then you can just download it in `Release page`[](photos/brave_9wjVE6BPbU.png). On how to change the safe you can read in the section "how to use script" under \*5.\* step.

# How to use the script

Firstly, you need to download a zip file from `Release page`[](photos/brave_9wjVE6BPbU.png).

Before we start, you need a `profile.json` file of your own. This file is what we going to change and it is what game uses to see, what events have you seen. If you dont want to use your own `profile.json` file and want to use a completly new one, then skip this step, since one completly blank `profile.json` file is alredy in the folder of the project.