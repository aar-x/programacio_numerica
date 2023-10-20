import numpy as np
from sklearn.datasets import load_iris

iris = load_iris()
data = iris.data
especies = iris.target
noms = iris.target_names

tipus, mostra = np.unique(especies, return_counts = True)

x = 0

print("\nTamany de les mostres")
print("---------------------")
while x < 3:
    print(noms[x].capitalize()+': '+str(mostra[x]))
    x += 1
print('')

#Troba l'espècie amb el valor màxim mitjana de la variable "sepal length (cm)"

x = 0
v_max = 0
x_max = 0
mitges_sepals = np.empty(3)

while x < 3:
    mitges_sepals[x] = np.round(np.mean(data[:(50+50*x), 0]), 2)
    if mitges_sepals[x] > v_max:
        v_max = mitges_sepals[x]
        x_max = x
    x += 1

print('Espècie mitjana longitud sèpals màxima')
print('--------------------------------------')
print(str(noms[x_max].capitalize())+': '+str(v_max)+'\n')
