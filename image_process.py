import os
import pyautogui
import pytesseract
import calculations 
import win32gui, win32con
from PIL import Image, ImageOps


class GearImage:
    def __init__(self):
        self.gear_path = os.getcwd() + "/gear_info/substats.png"
        self.screenshot = self.get_screenshot()
    

    def get_screenshot(self):
        hwnd = win32gui.FindWindow(None, "Corvus Simulator")
        screenshot = None
        if hwnd:
            win32gui.SetForegroundWindow(hwnd)
            # x, y, x1, y1 = win32gui.GetClientRect(hwnd)
            # x, y = win32gui.ClientToScreen(hwnd, (x, y))
            # x1, y1 = win32gui.ClientToScreen(hwnd, (x1 - x, y1 - y))
            # im = pyautogui.screenshot(region=(x, y, x1, y1)) # FOR WINDOWED NONFULLSCREEN? 
            screenshot = pyautogui.screenshot()
            hwnd = win32gui.FindWindow(None, "Corvus Simulator")
            win32gui.SetForegroundWindow(hwnd)
        else:
            print('Window not found!')

        # EDIT SCREENSHOT
        screenshot = ImageOps.autocontrast(ImageOps.grayscale(screenshot), cutoff = 2)
        screenshot.save(self.gear_path)
        text = pytesseract.image_to_string(self.gear_path, config = "--psm 6")
        # print(text)
        return screenshot

