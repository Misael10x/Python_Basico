import numpy as np
import plotly.express as px

np.random.seed(42)
x = np.random.rand(100)
y = np.random.rand(100)
sizes = np.random.rand(100) * 100
colors = np.random.rand(100)

fig = px.scatter(x=x, y=y, size=sizes, color=colors, 
                 title="Gráfico Interactivo de Dispersión",
                 labels={'x': 'Eje X', 'y': 'Eje Y'})

fig.show()
