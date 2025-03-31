import math

def velocidad_caida_libre():
    g = 9.81  
    h = float(input("Introduce la altura desde la que cae el objeto (m): "))
    
    if h < 0:
        print("\nLa altura no puede ser negativa.")
