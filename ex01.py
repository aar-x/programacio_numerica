from sklearn.datasets import load_iris

iris = load_iris()
data = iris.data
target = iris.target

print(data[:10])
print(target[:10])
