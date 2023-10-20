import numpy as np
from numpy import random
from sklearn.datasets import load_iris

iris = load_iris()
long_sepals = iris.data[:,0]
long_petals = iris.data[:,2]

mostra_long_sepals = random.choice(long_sepals, size=(20))
mostra_long_petals = random.choice(long_petals, size=(20))

print("\nMostra longitud sepals")
print('----------------------')
print(str(mostra_long_sepals))
print("\nMostra longitud petals")
print('----------------------')
print(str(mostra_long_petals)+'\n')
