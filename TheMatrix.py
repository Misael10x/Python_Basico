import random
import time
import os

def matrix_effect(width=80, height=20, speed=0.05):
    chars = "01X#*@"
    columns = [0] * width
