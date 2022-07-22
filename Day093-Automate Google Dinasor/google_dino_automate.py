import pyautogui
from PIL import ImageGrab
import time


def hit(key):
    pyautogui.press(key)
    return


def is_collide(data):
    # Draw the rectangle for cactus
    for i in range(710, 800):
        for j in range(275, 300):
            if data[i, j] < 100:
                hit("up")
                return
    # Draw the rectangle for birds
    for i in range(710, 800):
        for j in range(150, 275):
            if data[i, j] < 100:
                hit("down")
                return
    return


if __name__ == "__main__":
    print("Hey.. Dino game about to start in 3 seconds")
    time.sleep(3)
    # hit('up')

    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        is_collide(data)
        # Draw the rectangle for cactus
        # for i in range(710,800):
        #     for j in range(270, 300):
        #         data[i, j] = 0
        #
        # # Draw the rectangle for birds
        # for i in range(710, 800):
        #     for j in range(150, 265):
        #         data[i, j] = 171
        #
        # image.show()
        # break
