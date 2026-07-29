import mss
import cv2
from correction_list import comon_words
import numpy as np
import easyocr
import pyautogui as pg

"""
This is just a test file for ocr.
"""

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
        allowlist='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz 1234567890',
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

while True:
    print (ocr())