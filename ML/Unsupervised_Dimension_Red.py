# Dimension reduction is technique to find pattern in data and re-express it in compressed forms.
# Benefit:
#   More efficient storage and computation
#   Remove less informative "noise" features
# PCA is a technique of Dimension reduction - Principal Component Analysis
# PCA Steps - Decorrelation & Reduce Dimension
# Decorrelation rotates data samples to be aligned with axes and also shifts the mean to be 0
# Principal Components are directions of variance and PCA aligns principal components with the axes

from sklearn.datasets import load_wine
import pandas as pd
from scipy.stats import pearsonr
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# setting below help to view complete dataframe in one view. Try commenting below 3 lines and see the output
pd.set_option('display.max_columns', None)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('max_colwidth', -1)

wine = load_wine()
print(wine.keys())

wine_df = pd.DataFrame(wine.data, columns=wine.feature_names)
# print(wine_df.head())

corr, pvalue = pearsonr(wine_df['alcohol'], wine_df['malic_acid'])
# print(corr)

v_corr = wine_df.corr().round(decimals=2)
# print(v_corr)

# PCA for - total_phenols, flavanoids which is highly co-related by default

dataset = wine_df[['total_phenols', 'flavanoids']]
print(dataset.head())

model = PCA() # here we can define n_components attribute to define how many features to be retained
# the explained_variance_ attribute of PCA fit_transform menthod gives the variance of each feature in desc order
pca_features = model.fit_transform(dataset)

# Assign 0th column of pca_features: xs
xs = pca_features[:,0]

# Assign 1st column of pca_features: ys
ys = pca_features[:,1]

# Scatter plot xs vs ys
plt.scatter(xs, ys)
plt.axis('equal')
plt.show()

# Calculate the Pearson correlation of xs and ys
correlation, pval = pearsonr(xs, ys)

# Display the correlation
print(correlation)

# Intrinsic Dimensions: num of features needed to approximate the dataset
# The first principal component of the data is the direction in which the data varies the most.

mean = model.mean_
first_pc = model.components_[0:1]
# print(dataset.iloc[:, 0])
print(mean)
print(type(first_pc))
plt.scatter(dataset.iloc[:, 0], dataset.iloc[:, 1])
# Plot first_pc as an arrow, starting at mean
plt.arrow(mean[0], mean[1], first_pc[0][0], first_pc[0][1], color='red', width=0.01)

# Keep axes on same scale
plt.axis('equal')
plt.show()
