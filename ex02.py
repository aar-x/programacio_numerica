import numpy as np
from sklearn.datasets import load_iris

iris = load_iris()
data = iris.data
target = iris.target.reshape(150, 1)
data_target = np.concatenate((data, target), axis=1)

print('\ndata_target')
print('-----------')
print('')
print(data_target[:5])
print('')
