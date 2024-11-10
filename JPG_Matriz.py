from PIL import Image
import numpy as np

image_path = 'hola.jpg'  
img = Image.open(image_path)

img_resized = img.resize((3, 3))

img_matrix = np.array(img_resized)

print("Matriz 3x3 de la imagen:")
print(img_matrix)
