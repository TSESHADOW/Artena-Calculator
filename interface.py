import os # fix import
import calculations
import image_process
import tkinter as tk

import pytesseract
import cv2


class Application:
    def __init__(self, parent):
        self.parent = parent
        self.setup()

        # self.frame = tk.Frame(self.parent, height = 600, width = 300)
        # self.frame.pack()
        
    
    def setup(self):
        s = tk.ttk.Style()
        s.configure('.', font=('Helvetica', 13, 'bold'))
        w = self.parent.winfo_screenwidth()
        h = self.parent.winfo_screenheight()
        self.parent.geometry("300x600+%d+%d" % (w * (83/100), h * (18/100)))
        self.parent.title("Artena Calculator ver. 0.5")
        self.parent.iconbitmap("assets/artena.ico")

        self.bg = tk.PhotoImage(file = os.getcwd() + "/assets/artena.png") # saves background image to self 
        artena_label = tk.Label(self.parent, image = self.bg)
        artena_label.place(relx = 1, rely = 0, anchor = "ne")

        calculate_button = tk.ttk.Button(text="Calculate", command = self.get_image)
        calculate_button.place(relx = 0, rely = 0.00095, height = 50, width = 123, anchor = "nw")

        self.bottom_text = tk.StringVar(self.parent)
        gearscore_label = tk.Label(self.parent, textvariable = self.bottom_text, font = ("Helvetica", 13, "bold"), justify = "left")
        gearscore_label.place(relx = 0, rely = 0.35)

        self.parent.attributes('-topmost', True)


    def calculate_from_text(self, text):
        steps, score = calculations.calculate(text) # SPLIT JUST IN CASE SCORE IS NEEDED IN THE FUTURE
        # self.image.screenshot.show()

        self.bottom_text.set("{}\nFinal Gearscore: {}".format(steps, score))     


    def get_image(self):
        self.image = image_process.GearImage()
        width, height = self.image.screenshot.size
        # print("GOT IMAGE")
        # print(width, height)

        # RESCREENSHOT TO CAPTURE SUBSTATS
        # CURRENTLY WORKS ON INVENTORY GEAR ONLY 

        self.image.screenshot = self.image.screenshot.crop((width * (26.7/100), height * (53/100), width * (47/100), height * (72/100)))
        self.image.screenshot.save(self.image.gear_path)
        text = pytesseract.image_to_string(self.image.gear_path, config = "--psm 6")
        text = text.split('\n')
        self.calculate_from_text(text)
        # self.image.screenshot.show()
