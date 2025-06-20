import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

valores = []

fig, ax = plt.subplots()
linea, = ax.plot([], [], lw=2)

def init():
    ax.set_xlim(0, 50)
    ax.set_ylim(0, 100)
    return linea,

def actualizar(frame):
    if len(valores) >= 50:
        valores.pop(0)
    valores.append(random.randint(0, 100))
    linea.set_data(range(len(valores)), valores)
    return linea,

ani = animation.FuncAnimation(fig, actualizar, init_func=init, blit=True, interval=200)
plt.show()
