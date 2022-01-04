import keyboard
import cv2
import numpy as np
import pyautogui
import time

leftpixels = [(834, 641), (836, 631), (830, 635)]
rightpixels = [(1058, 636), (1054, 627), (1066, 648)]

time.sleep(3)
localeft = True
overhead = False


while True:
    if keyboard.is_pressed('q'):
        print("Bot stopped")
        break

    time.sleep(0.05)

    # find branch over current location
    if localeft == True:
        # search the left side points
        p1 = pyautogui.pixel(leftpixels[0][0], leftpixels[0][1])
        p2 = pyautogui.pixel(leftpixels[1][0], leftpixels[1][1])
        p3 = pyautogui.pixel(leftpixels[2][0], leftpixels[2][1])
        # print(p1, p2, p3)
        if p1[2] < 70 or p2[2] < 70 or p3[2] < 70:
            print("detected in left")
            overhead = True
            p1, p2, p3 = 0, 0, 0

    elif localeft == False:
        # search the right side points
        p1 = pyautogui.pixel(rightpixels[0][0], rightpixels[0][1])
        p2 = pyautogui.pixel(rightpixels[1][0], rightpixels[1][1])
        p3 = pyautogui.pixel(rightpixels[2][0], rightpixels[2][1])
        # print(p1, p2, p3)

        if p1[2] < 70 or p2[2] < 70 or p3[2] < 70:
            print("detected in right")
            overhead = True
            p1, p2, p3 = 0, 0, 0

    if overhead:
        # change loca to other side
        if localeft == True:
            localeft = False

        else:
            localeft = True

        # press current location

        if localeft == True:
            pyautogui.press("left")
            print("left")
        else:
            pyautogui.press("right")
            print("right")
        overhead = False
    else:
        # press current location
        if localeft == True:
            pyautogui.press("left")
            print("left")
        else:
            pyautogui.press("right")
            print("right")
