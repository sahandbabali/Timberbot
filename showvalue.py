
import cv2
import numpy as np
import pyautogui
import time


leftpixels = [(834, 641), (836, 631), (830, 635)]
rightpixels = [(1058, 636), (1054, 627), (1066, 648)]

print("left")
print(pyautogui.pixel(leftpixels[0][0], leftpixels[0][1]))
print(pyautogui.pixel(leftpixels[1][0], leftpixels[1][1]))
print(pyautogui.pixel(leftpixels[2][0], leftpixels[2][1]))

print("right")
print(pyautogui.pixel(rightpixels[0][0], rightpixels[0][1]))
print(pyautogui.pixel(rightpixels[1][0], rightpixels[1][1]))
print(pyautogui.pixel(rightpixels[2][0], rightpixels[2][1]))