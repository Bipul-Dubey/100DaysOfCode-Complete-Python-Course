import pyautogui
from PIL import Image,ImageGrab
import time


def hit(key):
    pyautogui.keyDown(key)
    return


def is_collide(data):
    # for Birds
    for i in range(530, 560):
        for j in range(80,127):
            if data[i, j] < 171:
                hit('down')
                return
    # for Cactus
    for i in range(530,620):
        for j in range(130,160):
            if data[i,j]<100:
                hit('up')
                return
    return


if __name__=='__main__':
    print('Hey Google Dinosaur Game Start.........')
    time.sleep(3)
    hit('up')
    while True:
        image=ImageGrab.grab().convert('L')
        data=image.load()
        is_collide(data)
