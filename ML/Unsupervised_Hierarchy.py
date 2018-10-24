# agglomerative - combining near clusters into one cluster such that it ultimately end into one cluster with a
# hierarchical structure

# Perform the necessary imports
from scipy.cluster.hierarchy import linkage, dendrogram, fcluster
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

iris = load_iris()
samples = iris.data
# Calculate the linkage: mergings
mergings = linkage(samples, method='complete')

"""
the linkage method defines how the distance between clusters is measured. In complete linkage, the distance between 
clusters is the distance between the furthest points of the clusters. In single linkage, the distance between clusters 
is the distance between the closest points of the clusters.
"""

# Plot the dendrogram, using varieties as labels
dendrogram(mergings,
           labels=iris.target,
           leaf_rotation=0,
           leaf_font_size=6,
)
plt.show()

labels = fcluster(mergings, 6, criterion='distance')
print(labels)

# t-SNE = t-distributed stochastic neighbor embedding

"""
# Import TSNE
from sklearn.manifold import TSNE

# Create a TSNE instance: model
model = TSNE(learning_rate=200)

# Apply fit_transform to samples: tsne_features
tsne_features = model.fit_transform(samples)

# Select the 0th feature: xs
xs = tsne_features[:,0]

# Select the 1st feature: ys
ys = tsne_features[:,1]

# Scatter plot, coloring by variety_numbers
plt.scatter(xs, ys, c=variety_numbers)
plt.show()

"""
