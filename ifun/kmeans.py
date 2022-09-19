import numpy as np
import matplotlib.pyplot as plt

X = np.random.rand(100, 2)
X[0]

plt.scatter(X[:, 0], X[:, 1], s = 50)

from sklearn.cluster import KMeans
clf = Kmeans(n_clusters = 3)
clf.fit(X)

clf.labels_
plt.scatter(X[:, 0], X[:, 1], c = clf.labels_)