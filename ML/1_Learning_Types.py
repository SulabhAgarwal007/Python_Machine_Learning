"""
Machine learning is art and science of giving computers ability to learn from data without being programmed explicitly

Unsupervised Learning: (Used Unlabeled Data) - Uncovering hidden patterns from unlabeled data. for e.g. classification
                        into some categories (called as clustering) without knowing the categories beforehand.
Reinforcement Learning: Software agents interacts with an environment and learn how to optimize their behaviour.
                        This type to learning has major implementations in the field of behavioural sycopathy.
Supervised Learning: Used Labeled Data
    - Predictor Variables/Features/independent variable and Target Variable/dependent variable/response variable.
     Aim here remains to predict the target variable given the predictor variable.
        - Classification: If Target Variable is discrete or consists of categories.
        - Regression: If Target Variable is continuous

    - For supervised learning we need labeled data which can be received by below techniques:
        - Historical data with labels
        - experiments to get label data
        - crowd-sourcing labeled data

Exploratory Data Analysis:
To observe the patterns in data from initial data or visual analysis like by plotting.

The Classification Challenge: kNN - k Nearest Neighbour
It's a classification algorithm which divides the data set into logical boundaries to classify the data based on nearest
data points.


.fit() - to fit our training data into the model
.predict() - to predict the data from test data.
"""

from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('ggplot')
iris = datasets.load_iris()

X = iris.data
Y = iris.target

# print(iris.feature_names)

df = pd.DataFrame(X, columns=iris.feature_names)
df_training = df.loc[:140, :]
print(df_training.info())

df_test = df.loc[141:, :]
print(df_test.info())

X_train = df_training.values
Y_train = Y[0:141]

X_test = df_test.values
Y_test = Y[141:]

knn = KNeighborsClassifier(n_neighbors=6)

knn.fit(X_train, Y_train)

Y_predict = knn.predict(X_test)

print(Y_predict, Y_test)

"""
In classification problems the metric for measuring model performance is Accuracy
Accuracy = Fraction of correct predictions
"""