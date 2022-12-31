import os
import cv2
import pyautogui
import pytesseract
import calculations 
import win32gui, win32con
from detect import detect
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
            hwnd = win32gui.FindWindow(None, "Artena Calculator ver. 0.5")
            win32gui.SetForegroundWindow(hwnd)
        else:
            print('Window not found!')

        # EDIT SCREENSHOT - put in another function
        # width, height = screenshot.size
        # screenshot = screenshot.crop((width * (26.7/100), height * (53/100), width * (47/100), height * (72/100)))

        # width, height = screenshot.size

        # screenshot = screenshot.resize((width * 3, height * 3)) 
        # screenshot = ImageOps.autocontrast(ImageOps.grayscale(screenshot), cutoff = 2)
        screenshot.save(self.gear_path)
        image, top_left, bottom_right = detect(self.gear_path)
        cropped_image = image[top_left[1]: (bottom_right[1]), top_left[0] : (bottom_right[0])]
        im = Image.fromarray(cropped_image)
        width, height = im.size
        im = im.resize((width * 3, height * 3)) 
        im = ImageOps.autocontrast(ImageOps.grayscale(im), cutoff = 2)
        im.save(self.gear_path)
        
        #cv2.imshow("Image", cropped_image)
        # text = pytesseract.image_to_string(self.gear_path, config = "--psm 6")
        # print(text)
        
        return im # only saves cropped stats into self.screenshot

