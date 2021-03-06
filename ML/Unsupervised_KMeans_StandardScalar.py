from sklearn import datasets
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import Normalizer

iris = datasets.load_iris()
print(iris.data.shape)
print(iris.target[0:5])

ks = range(1, 6)
inertias = []

for k in ks:
    # Create a KMeans instance with k clusters: model
    model = KMeans(n_clusters=k)

    # Fit model to samples
    model.fit(iris.data)

    # Append the inertia to the list of inertias
    inertias.append(model.inertia_)

# Plot ks vs inertias
plt.plot(ks, inertias, '-o')
plt.xlabel('number of clusters, k')
plt.ylabel('inertia')
plt.xticks(ks)
# plt.show()

# from above we can see that n_clusters = 3 would be appropriate cluster as intetia is getting flattening post 3

final_model = KMeans(n_clusters=3)
scalar = StandardScaler()
pipeline = make_pipeline(scalar, final_model)

pipeline.fit(iris.data)
labels = pipeline.predict(iris.data)

print(labels.shape)
plt.scatter(iris.data[:, 0], iris.data[:, 2], c=labels)
plt.scatter(iris.data[:, 0], iris.data[:, 2], c=iris.target)
# plt.show()

df = pd.DataFrame({'labels':  labels, 'variety': iris.target})
df['Species'] = pd.Series(iris.target).map(dict(zip(range(3), iris.target_names)))

ct = pd.crosstab(df['labels'], df['Species'])
print(ct.head())

# print(iris.keys()) # 'data', 'target', 'target_names', 'DESCR', 'feature_names'
# print(iris.data[0:5])
# print(iris.target_names)

# With Normalizer
print('\n Normalizer')
norm = Normalizer()
pipeline2 = make_pipeline(norm, final_model)
pipeline2.fit(iris.data)
labels2 = pipeline2.predict(iris.data)

df2 = pd.DataFrame({'labels':  labels2, 'variety': iris.target})
df2['Species'] = pd.Series(iris.target).map(dict(zip(range(3), iris.target_names)))

ct2 = pd.crosstab(df2['labels'], df2['Species'])
print(ct2.head())
