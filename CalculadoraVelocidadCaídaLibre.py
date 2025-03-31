import math

def velocidad_caida_libre():
    g = 9.81  
    h = float(input("Introduce la altura desde la que cae el objeto (m): "))
    
    if h < 0:
        print("\nLa altura no puede ser negativa.")
    else:
        v = math.sqrt(2 * g * h)
        print(f"\nVelocidad final: {v:.2f} m/s")

if __name__ == "__main__":
    velocidad_caida_libre()
