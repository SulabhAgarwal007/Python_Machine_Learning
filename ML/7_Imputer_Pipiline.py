"""
there are many steps to building a model, from creating training and test sets, to fitting a classifier or regressor,
to tuning its parameters, to evaluating its performance on new data. Imputation can be seen as the first step of this
machine learning process, the entirety of which can be viewed within the context of a pipeline. Scikit-learn provides a
pipeline constructor that allows you to piece together these steps into one process and thereby simplify your workflow.
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import Imputer  # for filling missing values based on different strategies
from sklearn.svm import SVC  # Support Vector Classifier
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

col_name = ['party', 'infants', 'water', 'budget', 'physician', 'salvador', 'religious', 'satellite', 'aid', 'missile',
            'immigration', 'synfuels', 'education', 'superfund', 'crime', 'duty_free_exports', 'eaa_rsa']

pd.set_option('display.max_columns', None)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('max_colwidth', -1)

df = pd.read_csv('house-votes-84.csv', names=col_name)

df = df.replace({'y': 1, 'n': 0, '?': np.nan})

print(df.isnull().sum())  # this gives total number of missing values in each column

y = df.party
X = df.drop('party', axis=1)

# Setup the Imputation transformer: imp
imp = Imputer(missing_values='NaN', strategy='most_frequent', axis=0)

# Instantiate the SVC classifier: clf
clf = SVC()

# Setup the pipeline with the required steps: steps
steps = [('imputation', imp), ('SVM', clf)]

# Create the pipeline: pipeline
pipeline = Pipeline(steps)


# Create training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Fit the pipeline to the train set
pipeline.fit(X_train, y_train)

# Predict the labels of the test set
y_pred = pipeline.predict(X_test)

# Compute metrics
print(classification_report(y_test, y_pred))

