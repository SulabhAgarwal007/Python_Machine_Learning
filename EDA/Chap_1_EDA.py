"""
EDA: Exploratory Data Analysis, which means before we do any hypothesis tests we should understand our data first
    by creating simple informative plots.
"""


from sklearn.datasets import load_iris
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


data = load_iris()
#print(data.keys())

df = pd.DataFrame(data.data, columns=data.feature_names)
(df.info())

iris_csv = pd.read_csv('iris.csv', sep=',')
#print(iris_csv.info())

sns.set()

bin_edge = [4, 4.4, 4.8, 5.2, 5.6, 6, 6.4, 6.8, 7.2, 7.6, 8, 8.4]
# How to decide number of bins:
#n_data = len(np.array(iris_csv['Sepal_length']))
n_data = len(iris_csv.values)
n_bins = int(np.sqrt(n_data))

# here _ is s dummy variable as we need only the plot while hist returns 3 vars.
_ = plt.hist(iris_csv['Sepal_length'], bins=n_bins)
_ = plt.xlabel('Sepal Length')
_ = plt.ylabel('Number of Samples')

plt.show()

# Histograms can deceive as information may change based on number of bins also called Bin Baising.
# Hence Swarm plot can be a option

_ = sns.swarmplot(x='Class', y='Sepal_length', data=iris_csv)
_ = plt.xlabel('Class')
_ = plt.ylabel('Sepal Length')

plt.show()

# ECDF - Empirical Cumulative Distribution Function
# Swamplots can become indecisive with too much of data. Hence ECDF can give better picture.
# Here we need to sort our data using numpy
Setosa_df = iris_csv.loc[iris_csv['Class'] == 'Iris-setosa']
Versicolor_df = iris_csv.loc[iris_csv['Class'] == 'Iris-versicolor']
Virginica_df = iris_csv.loc[iris_csv['Class'] == 'Iris-virginica']

x_set = np.sort(Setosa_df['Sepal_length'])
y_set = (np.arange(1, len(x_set)+1)*100)/len(x_set)
# here y represents percentage of x values lying below a certain value of x

x_ver = np.sort(Versicolor_df['Sepal_length'])
y_ver = (np.arange(1, len(x_ver)+1)*100)/len(x_ver)

x_vir = np.sort(Virginica_df['Sepal_length'])
y_vir = (np.arange(1, len(x_vir)+1)*100)/len(x_vir)

_ = plt.plot(x_set, y_set, marker='.', linestyle='none')
_ = plt.plot(x_ver, y_ver, marker='.', linestyle='none')
_ = plt.plot(x_vir, y_vir, marker='.', linestyle='none')
_ = plt.xlabel('Sepal Length')

# calculating percentiles and plotting on ECDF
percentiles = np.array([2.5, 25, 50, 75, 97.5])
x_set_perct = np.percentile(x_set, percentiles)
x_ver_perct = np.percentile(x_ver, percentiles)
x_vir_perct = np.percentile(x_vir, percentiles)

_ = plt.plot(x_set_perct, percentiles, marker='D', color='blue', linestyle='none')
_ = plt.plot(x_ver_perct, percentiles, marker='D', color='green', linestyle='none')
_ = plt.plot(x_vir_perct, percentiles, marker='D', color='red', linestyle='none')

plt.tight_layout()
plt.show()

"""Some basic statistics
Mean = average of set of values (np.mean)
Median = Middle of a set of values (np.median)
Variance = Mean of squared difference of value with mean (np.var)
Std. Deviation = square root of variance (np.std)
Co-variance = relation between two variables. ((x-X)(y-Y))/n where X and Y are respective means (np.cov)
    For e.g. If we have two sets of data x and y, np.cov(x, y) returns a 2D array where entries [0,1] and [1,0] are the 
    covariances. Entry [0,0] is the variance of the data in x, and entry [1,1] is the variance of the data in y. 
    This 2D output array is called the covariance matrix, since it organizes the self- and covariance.
Pearson Co-Relation Coefficient = Co-variance/Std_X*Std_Y (np.corrcoef())
"""