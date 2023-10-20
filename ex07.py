import numpy as np
from sklearn.datasets import load_iris

iris = load_iris()
data = iris.data

# 7.1. Calcula la matriu de correlació entre les variables.

data_transpuesta = np.transpose(data)
print('\n7.1 Matriu de correlacions entre les 4 característiques:\n')
print(np.corrcoef(data_transpuesta))

# 7.2. Filtra els valors majors a la mitjana de la longitud dels pètals i mostra-ho.

mitja = np.round(np.mean(data[:,2]), 3)

# Valors majors a la mitjana

majors_mitja = np.array([])

for x in data:
    if (x[2] > mitja):
        majors_mitja = np.append(majors_mitja, x[2])

# Impressió valors

print('\n7.2 Pètals més llargs que la mitjana')
print('\nMitjana: '+str(mitja)+' cm.')
print('\nValors més grans:\n\n'+str(majors_mitja)+'\n')

# 7.3. Troba la mostra amb els pètals més grans.

major_petal = np.amax(majors_mitja)
print('7.3 Pètal més llarg de tots: '+str(major_petal)+' cm.\n')
