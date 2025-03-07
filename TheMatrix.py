import random
import time
import os

def matrix_effect(width=80, height=20, speed=0.05):
    chars = "01X#*@"
    columns = [0] * width
    
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        for i in range(height):
