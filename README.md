
# Tavern NSFW Builder for [Tales of Androgyny](https://majalis.itch.io/tales-of-androgyny)

`Version 0.1`

Tavern NSFW Builder is a Python script repository made for the game [Tales of Androgyny](https://majalis.itch.io/tales-of-androgyny).

It is designed to create 100% complete save files (**excluding achievements**) for theoretically every version of the game (even future ones! ... *hopefully*).

# How does it work?

The project is based on OCR (Optical Character Recognition) and uses **PyAutoGUI** together with **pynput** to simulate user input.

The script abuses the **Progress** page in the main menu to scan the **Unseen Events** section with OCR and automatically add those events to the save file. Since it reads event names directly from the game, it should also work with future game versions, even for events that nobody has seen before as long as OCR recognizes the event names correctly (or the built-in correction system is able to fix the mistakes).

# Save file

During testing, I used this script to generate a save file with 100% completion.

If you only need a 100% save file (**achievements are not fully unlocked**) for version **0.3.69**, you can simply download it from the [`Releases`](https://github.com/stopexstra/Tavern-NSFW-builder/releases) page.

Instructions for replacing your save file can be found in **Step 2** of the "How to use the script?" section.

# How to use the script

0. Install Python. This project requires Python. If you don't already have it installed, [download it first](https://stackoverflow.com/questions/52578270/install-python-with-cmd-or-powershell).

1. Download the latest `Tavern_NSFW_Builder.zip` from the [`Releases`](https://github.com/stopexstra/Tavern-NSFW-builder/releases) page and extract it to any folder you like.

2. Before running the script, you'll need your own `profile.json` file. This file stores your game progress and determines which events have already been seen.
If you don't want to use your own save file and instead want to use either the provided 100% save (v0.3.69) or start from a completely blank save, you can skip this step. A blank `profile.json` is already included in the project.
- On Windows, press **Win + R**, type `appdata`, and click [ok](photos/explorer_bRi8tVJUal.png)
- Navigate to `Roaming/TalesOfAndrogyny`.
- Copy `profile.json` into [project folder](photos/explorer_t6OGn1cJdS.png), replacing the existing file.

If `profile.json` does not exist in `Roaming/TalesOfAndrogyny`, it simply means you don't have a save file yet. In that case, you can either use the provided 100% save for v0.3.69 or the blank save included with the project.

3. Once you've copied your own `profile.json` (or decided to use the provided one), you're ready to start.
- Open the game.
- Press **Alt + Tab** back to the project folder.

4. Right-click inside the project folder and open a [terminal](photos/explorer_ad6RPzJUMV.png).

Run:

```
python .\Tavern-NSFW-builder.py
```

5. Return to the game. After a few seconds, the script will start its scanning [loop](photos/explorer_qnYE5ctI1o.gif). By default, it will continue running until you press **Q** or **Esc**. (You can change these pattern and hotkeys in the code. On how to do it, look the section "How to customize the script") Let the script run. How long the process takes depends on your computer and on how many unseen events remain.

6.  Once the scanning loop has finished (or you've stopped it manually), return to the terminal and run:

```
python .\final_correction.py
```

After a second, you'll see a large amount of text printed in the terminal. This is completely normal—it is only a log of the performed corrections. Run this command repeatedly until the only output is:
```
Finished!
```
(photos/WindowsTerminal_Jg61LbJ8Vc.png)

> [!WARNING]
> If, after running this command **3–5 times**, the output still does not become just **"Finished!"**, then something has gone wrong.
>
> You can either ignore the issue and continue with this guide (some events may remain marked as **unseen**), or you can try to fix it manually. See the **"Common Errors"** section for possible solutions.


7. A new file called `database_generated.json` will appear in the project folder.

Go back to:

`AppData\Roaming\TalesOfAndrogyny`

Delete your existing `profile.json`, then copy `database_generated.json` into that folder and rename it to:

`profile.json`

8. Done! Launch the game again, open the **Progress** page, and enjoy your updated completion progress.

# How to customize the script

Hey! If you're reading this, it means I haven't finished writing this section yet.

I'll add it as soon as I can. :)

# Common Errors

Hey! If you're reading this, it means I haven't finished writing this section yet.

I'll add it as soon as I can. :)
