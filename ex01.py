from sklearn.datasets import load_iris

iris = load_iris()
data = iris.data
target = iris.target

print('\nDATA')
print('----')
print(data[:10])
print('\nTARGET')
print('------')
print(str(target[:10])+'\n')
