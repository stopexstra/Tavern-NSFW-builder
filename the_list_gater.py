import mss
import cv2
from correction_list import comon_words
import numpy as np
import easyocr
import pyautogui as pg
from pynput import keyboard
import time 
from shutil import copyfile
from json_manager import load_json, save_json, add_text

running = True

SOURCE_JSON = "profile.json"
OUTPUT_JSON = "database_generated.json"

copyfile(SOURCE_JSON, OUTPUT_JSON)

json_data = load_json(OUTPUT_JSON)

duplicate_count = 0

width, height = pg.size()

monitor = {
    "left": int(width * 0.61354), # 1178 / (width)1920 = 0.61354
    "top": int(height * 0.71759), # 775  / (height)1080 = 0.71759
    "width": int(width * 0.37031), # 711  / (width)1920 = 0.37031
    "height": int(height * 0.187962963) # 203  / (height)1080 = 0.187962963
}

coordinates = {
    "progress":(0.7567708333333333, 0.2953703703703704),
    "done":(0.884375, 0.9175925925925926),
    "color_check":(0.8515625, 0.8796296296296297),
    "color_check_slide": (0.2421875, 0.5546296296296296),
    "color_check_done": (0.5729166666666666, 0.8203703703703704)
}

def fix_text(text):
    for wrong, correct in comon_words.items():
        text = text.replace(wrong, correct)

    return text

reader = easyocr.Reader(['en'])

def ocr():
    sct = mss.MSS()
    screenshot = sct.grab(monitor)

    img = np.array(screenshot)
    img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)

    result = reader.readtext(
        img,
        allowlist='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz 1234567890'
    )

    result.sort(
        key=lambda d: (
            min(p[1] for p in d[0]),   # top
            min(p[0] for p in d[0])    # left
        )
    )

    lines = []
    Y_THRESHOLD = 10
    for detection in result:
        box = detection[0]
        text = fix_text(detection[1]).strip()
        if not text:
            continue
        left = min(p[0] for p in box)
        top = min(p[1] for p in box)

        found = False
        for line in lines:
            if abs(line["top"] - top) <= Y_THRESHOLD:
                line["parts"].append((left, text))
                found = True
                break

        if not found:
            lines.append({
                "top": top,
                "parts": [(left, text)]
            })

    texts = []

    for line in lines:
        line["parts"].sort(key=lambda x: x[0])
        sentence = " ".join(
            text
            for _, text in line["parts"]
        )
        texts.append(sentence)
    return texts

def onPress(key):
    global running

    try:
        match key.char:
            case "q":          
                print("Stopping...")
                running = False
    except AttributeError:
        if key == keyboard.Key.esc:
            print("Stopping...")
            running = False
"""
def onPress(key):
    try:
        match key.char:
            case "p":
                width, height = pg.size()
                x, y = pg.position()
                print (f"{x / width}, {y / height}")
                print (x, y, width, height)
                print (pg.pixel(x,y))
            case "m":
                moveMouse(coordinates["progress"][0], coordinates["progress"][1])
                pg.click()
            case "l":
                moveMouse(coordinates["done"][0], coordinates["done"][1])
                pg.click()
            case "t":
                moveMouse(0.8515625, 0.8796296296296297)
    except:
        pass
"""
    
def moveMouse(x, y, time=0.0):
    pg.moveTo(
        x * pg.size()[0],
        y * pg.size()[1],
        time
    )

listener = keyboard.Listener(on_press=onPress)
listener.start()

width, height = pg.size()

main_menu = False
slide_main_menu = False
done_menu = False

"""
while True:
    try:
        "sdf"
    except:
        pass
"""
#main loop

duplicate_count = 0        
total_duplicates = 0         

while running:
    x = int(coordinates["color_check_slide"][0] * width)
    y = int(coordinates["color_check_slide"][1] * height)

    if pg.pixelMatchesColor(x, y, (233, 185, 139), 50):
        slide_main_menu = True

    if slide_main_menu:
        pg.click()
        slide_main_menu = False

    x = int(coordinates["color_check"][0] * width)
    y = int(coordinates["color_check"][1] * height)

    if pg.pixelMatchesColor(x, y, (86, 189, 208), 50):
        main_menu = True

    if main_menu:
        time.sleep(0.15)
        moveMouse(coordinates["progress"][0], coordinates["progress"][1])
        pg.click()
        main_menu = False
        done_menu = True
    
    x = int(coordinates["color_check_done"][0] * width)
    y = int(coordinates["color_check_done"][1] * height)

    if done_menu or pg.pixelMatchesColor(x, y, (228, 209, 189), 50):
        time.sleep(0.15)
        texts = ocr()

        print(texts)

        if texts:

            for text in texts:

                #if len(text.split()) < 2:
                #    print(f"Ignoring one-word text: {text}")
                #    continue

                was_added = add_text(json_data, text)

                if was_added:
                    duplicate_count = 0
                    save_json(json_data, OUTPUT_JSON)
                    print("Added:", text)

                else:
                    duplicate_count += 1
                    total_duplicates += 1
                    print(f"Duplicate ({duplicate_count}/10), total: {total_duplicates}/1000 {text}")

                    #if duplicate_count >= 10 :
                    #    print("10 duplicates in a row. Stopping.")
                    #    exit()

                    #if total_duplicates >= 1000:
                    #    print("1000 total duplicates found. Stopping.")
                    #    exit()

            moveMouse(coordinates["done"][0], coordinates["done"][1])
            pg.click()
            done_menu = False