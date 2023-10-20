import numpy as np

from sklearn.datasets import load_iris
iris = load_iris()

long_sepals = iris.data[:,0]
mitja_long_sepals = np.around(np.mean(long_sepals), 2)
desv_long_sepals = np.around(np.std(long_sepals), 2)

print("\nMitjana longitud sèpals: "+str(mitja_long_sepals))
print("Desviació estàndard: "+str(desv_long_sepals)+'\n')

long_petals = iris.data[:,2]
mitja_long_petals = np.around(np.mean(long_petals), 2)
desv_long_petals = np.around(np.std(long_petals), 2)

print("Mitjana longitud pètals: "+str(mitja_long_petals))
print("Desviació estàndard: "+str(desv_long_petals)+'\n')
