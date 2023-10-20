import numpy as np
from sklearn.datasets import load_iris

iris = load_iris()
data = iris.data
x = 0
y = 0

mitges = np.zeros((3, 4))

while x < 3:
    while y < 4:
        mitges[x, y] = round(np.mean(data[(x*50):(x*50+50), y]), 2)
        y += 1
    x += 1
    y = 0

print("\nMitjana (per característica i espècie)\n")
print(mitges, end = '\n\n')

x = 0
y = 0

desv = np.zeros((3, 4))

while x < 3:
    while y < 4:
        desv[x, y] = np.round(np.std(data[(x*50):(x*50+50), y]), 2)
        y += 1
    x += 1
    y = 0


print("Desviacions típiques (idem)\n")
print(str(desv)+'\n')
