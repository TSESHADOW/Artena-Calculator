import pytesseract as tsc
import os
import time
import pyautogui
import tkinter as tk
from tkinter import *
from tkinter.filedialog import *
from PIL import Image 
import numpy as np  
import win32gui, win32con

hide = win32gui.GetForegroundWindow()
win32gui.ShowWindow(hide , win32con.SW_HIDE)


Puede = "85"
Refor = ""
Stats = ""
GearS = ""
teseconfig = "--psm 6 --oem 1 -c tessedit_char_blacklist={}()&®©«~;:,."
Direccion = os.getcwd()+"\\Gearscore"
Direccion2 = os.getcwd()+"\\Nivel"
root = tk.Tk()
root.title("Artena Calculator ver. 0.5")
root.geometry("300x600")
root.iconbitmap("artena.ico")



root.resizable(width=False, height=False)
bg = PhotoImage(file=os.getcwd()+"\\artena.png")


my_label = Label(root, image=bg)
my_label.place(x=125, y=0, width=175, height=200)



root.attributes('-topmost', True)



def purga(character, texto):
	index = texto.find(character)
	while index != -1:
		if texto[index-1]==" ":
			texto = texto[:index-1] + texto[index+1:]
		else:
			texto = texto[:index] + texto[index+1:]
		index = texto.find(character)
	return texto

def reemplazar (character, texto):
	index = texto.find(character)
	match character:
		case "a":
			while index != -1:
				texto = "3"
				index = texto.find("a")
		case "]":
			while index != -1:
				texto = "9"
				index = texto.find("]")
		
		case "iq":
			while index != -1:
				texto = "7"
				index = texto.find("iq")
		case "wf":
			while index != -1:
				texto = "11"
				index = texto.find("wf")
		case "T":
			while index != -1:
				texto = texto[:index] + "7" + texto[index+1:]
				index = texto.find("T")		
		case "ne":
			while index != -1:
				texto = "13"
				index = texto.find("ne")		
		case "si":
			while index != -1:
				texto = "31"
				index = texto.find("si")
		case "/":
			while index != -1:
				texto = texto[:index] + "7" + texto[index+1:]
				index = texto.find("/")
		case "i":
			while index != -1:
				texto = texto[:index] + "1" + texto[index+1:]
				index = texto.find("i")
		case "g":
			while index != -1:
				texto = texto[:index] + "9" + texto[index+1:]
				index = texto.find("g")
		case "&":
			while index != -1:
				texto = texto[:index] + "33" + texto[index+1:]
				index = texto.find("&")
		case default:
			print("no se encontró el caracter"+srt(int(character).hex()))
	return texto
	
def takeScreenshot2():
	global Refor
	Refor = "Refor"
	os.system("cls")
	myScreenshot = pyautogui.screenshot(region=(550,620, 600, 150))
	myScreenshot = myScreenshot.resize((2400,600))
	save_path = Direccion+"\\1.png"
	myScreenshot.save(save_path)
	ruta = Direccion
	img = Image.open(Direccion+"\\1.png").convert('RGB') 
  
	img_arr = np.array(img) 
  
	img_arr[0 : 800, 1300 : 1960] = (0, 0, 0) 
  
	img = Image.fromarray(img_arr) 
	img.save(save_path)
	ruta = Direccion
	lista = os.listdir(ruta)
	print(lista)
	substats = []
	for elemento in lista:
		if (elemento.split('.')[-1] in ('png')):
			texto = tsc.image_to_string(ruta+'\\'+elemento, config= teseconfig)
			texto = purga("«", texto)
			texto = purga("©", texto)
			texto = purga("®", texto)
			texto = purga(")", texto)
			texto = reemplazar("/", texto)
			texto = reemplazar("&", texto)
			array_texto = texto.split('\n')
			print(array_texto)
			for e in array_texto:
				if e != "":
					array_e = e.split(" ")
					if len(array_e)>2:
						array_e[0]= " ".join(array_e[:-1])
					print(array_e[0],array_e[-1])
					substats.append(array_e[0])
					substats.append(array_e[-1])
	calculo(substats)
	
def takeScreenshot():
	global Refor
	Refor = "Refo"
	os.system("cls")
	myScreenshot = pyautogui.screenshot(region=(60,425, 497, 165))
	myScreenshot = myScreenshot.resize((1988,660))
	save_path = Direccion+"\\1.png"
	myScreenshot.save(save_path)
	ruta = Direccion
	lista = os.listdir(ruta)
	print(lista)
	substats = []
	for elemento in lista:
		if (elemento.split('.')[-1] in ('png')):
			texto = tsc.image_to_string(ruta+'\\'+elemento, config= teseconfig)
			texto = purga("©", texto)
			texto = purga(")", texto)
			texto = reemplazar("/", texto)
			texto = reemplazar("&", texto)
			array_texto = texto.split('\n')
			print(array_texto)
			for e in array_texto:
				if e != "":
					array_e = e.split(" ")
					if len(array_e)>2:
						array_e[0]= " ".join(array_e[:-1])
					print(array_e[0],array_e[-1])
					substats.append(array_e[0])
					substats.append(array_e[-1])
	calculo(substats)
	
def takeScreenshot3():
	global Refor
	Refor = "Refo"
	os.system("cls")
	myScreenshot = pyautogui.screenshot(region=(100,425, 375, 160))
	myScreenshot = myScreenshot.resize((1500,640))
	save_path = Direccion+"\\1.png"
	myScreenshot.save(save_path)
	ruta = Direccion
	lista = os.listdir(ruta)
	print(lista)
	substats = []
	for elemento in lista:
		if (elemento.split('.')[-1] in ('png')):
			texto = tsc.image_to_string(ruta+'\\'+elemento, config= teseconfig)
			texto = purga("©", texto)
			texto = purga(")", texto)
			texto = reemplazar("/", texto)
			texto = reemplazar("&", texto)
			array_texto = texto.split('\n')
			print(array_texto)
			for e in array_texto:
				if e != "":
					array_e = e.split(" ")
					if len(array_e)>2:
						array_e[0]= " ".join(array_e[:-1])
					print(array_e[0],array_e[-1])
					substats.append(array_e[0])
					substats.append(array_e[-1])
	calculo(substats)
	

def calculo (substats):
	TankH = 0
	Dps = 0
	Bruiser = 0
	
	
	Stats = ""
	GearS = ""
	cuadro.delete("1.0","end-1c")
	Ataque = 0
	Defensa = 0
	Vida = 0
	Eficacia = 0
	Resistencia_a_efectos = 0
	Velocidad = 0
	Cdmg = 0
	Cc = 0
	Ataque_plano = 0
	Defensa_plana = 0
	Vida_plana = 0
	i=0
	while i<len(substats):	
		if substats[i].startswith("At"):
			substats[i]= "Attack"
		if substats[i].startswith("De"):
			substats[i]= "Defense"
		if substats[i].startswith("He") and substats[i].endswith("th"):
			substats[i]= "Health"
		if substats[i].startswith("Ef") and substats[i].endswith("ss"):
			substats[i]= "Effectiveness"
		if substats[i].startswith("Ef")and substats[i].endswith("ce"):
			substats[i]= "Effect Resistance"
		if substats[i].startswith("Sp") and substats[i].endswith("ed"):
			substats[i]= "Speed"	
		if substats[i].startswith("Cr") and substats[i].endswith("ge"):
			substats[i]= "Critical Hit Damage"
		if substats[i].startswith("Cr") and substats[i].endswith("ce"):
			substats[i]= "Critical Hit Chance"
		
		substats[i+1]=reemplazar("a", substats[i+1])
		substats[i+1]=reemplazar("]", substats[i+1])
		substats[i+1]=reemplazar("T", substats[i+1])
		substats[i+1]=reemplazar("ne", substats[i+1])
		substats[i+1]=reemplazar("wf", substats[i+1])
		substats[i+1]=reemplazar("g", substats[i+1])
		substats[i+1]=reemplazar("si", substats[i+1])
		substats[i+1]=reemplazar("iq", substats[i+1])
		substats[i+1]=reemplazar("i", substats[i+1])
		match substats[i]:
			case 'Attack':
				if substats[i+1][-1] == "%":
				
					Dps += 1
					
					Ataque = int(substats[i+1][:-1])
				else:
				
					Dps += 1
					
					Ataque_plano = int(substats[i+1])
			case 'NET':
				substats[i]= "Attack"
				if substats[i+1][-1] == "%":
					
					Dps += 1
					Bruiser += 1
				
					Ataque = int(substats[i+1][:-1])
				else:
					Dps += 1
					Ataque_plano = int(substats[i+1])
			case 'Defense':			
				if substats[i+1][-1] == "%":
				
					TankH += 1
					Bruiser += 1
					
					Defensa = int(substats[i+1][:-1])
				else:
					TankH += 1
					Defensa_plana = int(substats[i+1])
			case 'Health':	
				if substats[i+1][-1] == "%":
				
					TankH += 1
					Bruiser += 1
					
					Vida = int(substats[i+1][:-1])
				else:
					TankH += 1
					Vida_plana = int(substats[i+1])			
			case 'Effectiveness':
			
				Eficacia = int(substats[i+1][:-1])

			case 'Effect Resistance':
			
				TankH += 1
			
				Resistencia_a_efectos = int(substats[i+1][:-1])
			case 'Speed':
			
				TankH += 1
				Bruiser += 1
				Dps += 1
				
				Velocidad = int(substats[i+1])
			case 'Critical Hit Damage':
			
				Bruiser += 1
				Dps += 1
			
				Cdmg = int(substats[i+1][:-1])		
			case 'Critical Hit Chance':
			
				Bruiser += 1
				Dps += 1
			
				Cc = int(substats[i+1][:-1])	
			case other:
				print('No match found', substats[i])
				cuadro.delete("1.0","end-1c")
				cuadro.insert(tk.INSERT, "Gear not found                                     ")
		print(substats[i], substats[i+1])
		Stats = substats[i]+ " " +substats[i+1]+"\n"
		cuadro.insert(tk.INSERT, Stats)
		i+=2
	Score = Ataque \
	+ Defensa \
	+ Vida \
	+ Eficacia \
	+ Resistencia_a_efectos \
	+ Velocidad * (8/4) \
	+ Cdmg * (8/7)\
	+ Cc * (8/5)\
	+ Ataque_plano * 3.46 / 39\
	+ Defensa_plana * 4.99 / 31\
	+ Vida_plana * 3.09 / 174	
	
	print("Gear Score: "+str(Score))
	print("TABLE")
	print("+0: 24-32")
	print("+3: 30-37")
	print("+6: 36-42")
	print("+9: 42-46")
	print("+12: 48-50")
	GearS = ("\n"+"Gear Score: "+str(int(Score)))
	cuadro.insert(tk.INSERT, GearS)
		
	if Refor == "Refo" and Puede=="85":
		cuadro.insert(tk.INSERT, "\n"+"Reforged: "+str(int(Score)+11)+"-"+str(int(Score)+14)+" estimated")
	else:
		cuadro.insert(tk.INSERT, "\n"+"----------------------")
	cuadro.insert(tk.INSERT, "\n")
	if TankH == 4 or Dps == 4 or Bruiser == 4:
		if TankH == 4:
			cuadro.insert(tk.INSERT,"\n"+"Substats for Tank/Healer")
		if Dps == 4:
			cuadro.insert(tk.INSERT,"\n"+"Substats for Dps")
		if Bruiser == 4:
			cuadro.insert(tk.INSERT,"\n"+"Substats for Bruiser")
			
	if TankH == 3:
			cuadro.insert(tk.INSERT,"\n"+"Substats for Tank/Healer")
	if	Dps == 3:
			cuadro.insert(tk.INSERT,"\n"+"Substats for Dps")
	if Bruiser == 3:
			cuadro.insert(tk.INSERT,"\n"+"Substats for Bruiser")
		
	
	
	
	cuadro.insert(tk.INSERT, "\n")
	cuadro.insert(tk.INSERT, "\n"+"Left / Right:")
	cuadro.insert(tk.INSERT, "\n"+"Healer/Knight: 56 / 53 min.")
	cuadro.insert(tk.INSERT, "\n"+"Dps: 55 / 55 min.")
	cuadro.insert(tk.INSERT, "\n"+"Bruiser: 63 / 60 min.")
	cuadro.insert(tk.INSERT, "\n")
	cuadro.insert(tk.INSERT, "\n"+"                        TABLE")
	cuadro.insert(tk.INSERT, "\n"+"          +0: 24-32"+ "       +9: 42-46")
	cuadro.insert(tk.INSERT, "\n"+"          +3: 30-37"+ "       +12: 48-50")
	cuadro.insert(tk.INSERT, "\n"+"          +6: 36-42")
	
	
	

	
def nivelGear():
	global Puede
	texto = ""
	os.system("cls")
	myScreenshot2 = pyautogui.screenshot(region=(112,197, 37, 25))
	#myScreenshot2 = myScreenshot2.resize((1988,660))
	save_path = Direccion2+"\\1.png"
	myScreenshot2.save(save_path)
	ruta = Direccion2
	lista = os.listdir(ruta)
	substats = []
	for elemento in lista:
		if (elemento.split('.')[-1] in ('png')):
			texto = tsc.image_to_string(ruta+'\\'+elemento, config= teseconfig)
			texto = purga("©", texto)
			texto = purga(")", texto)
			texto = reemplazar("/", texto)
			texto = reemplazar("&", texto)
					
	cuadro.insert(tk.INSERT,"Extraje: "+texto)
	
	if texto.startswith("85"): 
		Puede = "85"
	else:
		Puede = "90"
	

def koyomi():
	cuadro.delete("1.0","end-1c")
	cuadro.insert(tk.INSERT, "Developed by TSESHADOW")
	cuadro.insert(tk.INSERT, "\n")
	cuadro.insert(tk.INSERT, "\n"+"Discord channel:")
	cuadro.insert(tk.INSERT, "\n"+"https://discord.gg/C7NMYPzt5s")
	cuadro.insert(tk.INSERT, "\n")
	cuadro.insert(tk.INSERT, "\n"+"If you want support me")
	cuadro.insert(tk.INSERT, "\n"+"here is my Paypal:")
	cuadro.insert(tk.INSERT, "\n"+"tseshadow@outlook.com.ar")
	
	cuadro.insert(tk.INSERT, "\n")
	cuadro.insert(tk.INSERT, "\n"+"If you want contact me")
	cuadro.insert(tk.INSERT, "\n"+"you can send me a PM:")
	cuadro.insert(tk.INSERT, "\n"+"TSESHADOW#3787")
	
	
myButton = tk.Button(text="Gear", command = lambda:[nivelGear(), takeScreenshot()], font = 10)
myButton2 = tk.Button(text="Reforge", command = takeScreenshot2, font = 10)
myButton3 = tk.Button(text="Leveling", command = lambda:[nivelGear(), takeScreenshot3()], font = 10)
myButton4 = tk.Button(text="Info", command = koyomi, font = 10)

cuadro = tk.Text(root, font = "helvetica 13 bold", foreground="white", background='#272727')
cuadro.place(x=0,y=200)


myButton.place(x=0, y=1, height= 50, width=125)
myButton3.place(x=0, y=51, height= 50, width=125)
myButton2.place(x=0, y=101, height= 50, width=125)
myButton4.place(x=0, y=151, height= 50, width=125)


root.mainloop()
root.update()