import re
import numpy as np  
from translate import Translator


SUBSTATS = {
    "Attack": 1, "Defense": 1, "Health": 1, "Effectiveness": 1, "Effect Resistance": 1, 
    "Critical Hit Damage": 8/7, "Critical Hit Chance": 8/5, 
    "Speed": 0    
}

FLAT_SUBSTATS = {
    "Attack": 3.46/39, "Defense": 4.99/31, "Health": 3.09/174, "Speed": 2
}

def calculate(text):
    translator = Translator(to_lang = 'en')
    steps = ""
    score = 0

    for line in text:
        temp = re.split('([-+]?\d+\.\d+)|([-+]?\d+)', line.strip())
        temp = [r.strip() for r in temp if r is not None and r.strip() != '']
        substat = [translator.translate(word) for word in temp]
        # print(substat)
        if substat and substat[0] in SUBSTATS:
            if substat[-1] != '%':
                temp_score = int(int(substat[1]) * FLAT_SUBSTATS[substat[0]] + 0.5)
                steps += "{} added {} gs.\n".format(substat[0], temp_score)
                score += temp_score

            else:
                temp_score = int(int(substat[1]) * SUBSTATS[substat[0]] + 0.5)
                steps += "{} % added {} gs.\n".format(substat[0], temp_score)
                score += temp_score

    print(steps)
    print("Final Gearscore: {}".format((score)))
    return (steps, score)
