import numpy as np
from sklearn.datasets import load_iris

iris = load_iris()
data = iris.data

# 8. Espècie amb la diferència més gran entre la longitud mitjana de sèpals i pètals.

mitjana_sepals = np.array([])
mitjana_petals = np.array([])
x = 0

# Un array para sépalos (con los tres tipos de flores) y otro para pétalos

while (x < 3):
    mitjana_sepals = np.append(mitjana_sepals, np.mean(data[50*x:(50+50*x),0]))
    mitjana_petals = np.append(mitjana_petals, np.mean(data[50*x:(50+50*x),2]))
    x += 1

# Cálculo de las diferencias

y = 0
val_max = 0
diferencia = mitjana_sepals - mitjana_petals

while (y<3):
    if diferencia[y] > val_max:
        val_max = diferencia[y]
        especie = iris.target_names[y]
    y += 1

print('\n8. Diferència màxima entre longitud de sèpals i pètals\n')
print(especie.capitalize()+': '+str(val_max)+' cm.\n')
