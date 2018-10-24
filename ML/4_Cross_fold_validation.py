"""
With normal R2 values for linear regression model, the value could be misleading as there can be some pecularities in
data impacting the R2 value. Hence a technique call k-fold CV is used (CV - Cross Validation)

Here the dataset is broken into k pieces and a R2 value is calculated k times. Every time, one partition is reserved for
testing and rest for training.
Later on we can do some more statistical operations on these R2 values.
"""

# Import necessary modules
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score
import numpy as np
import pandas as pd

df = pd.read_csv('gm_2008_region.csv')
y = df.fertility.values
X = df.drop(['fertility', 'Region'], axis=1).values

# Create a linear regression object: reg
reg = LinearRegression()

# Compute 5-fold cross-validation scores: cv_scores
cv_scores = cross_val_score(reg, X, y, cv=5)

# Print the 5-fold cross-validation scores
print(cv_scores)

print("Average 5-Fold CV Score: {}".format(np.mean(cv_scores)))

# If we increase cv then it will impact the performance. Use below in cmd window to see the loops and time taken
# %timeit cvscores_3 = cross_val_score(reg, X, y, cv=3)

#################Lasso Regularization
# Regularization is a technique where some penalty is added into the loss function based on the coefficients.
# There are 2 regularization techniques - Lasso and Ridge
# Lasso adds alpha*sum(absolute(coefficients))
# Ridge adds alpha*sum(square(coefficients))


# Import Lasso
from sklearn.linear_model import Lasso
import matplotlib.pyplot as plt

# Instantiate a lasso regressor: lasso
lasso = Lasso(alpha=0.4, normalize=True)

# Fit the regressor to the data
lasso.fit(X, y)

# Compute and print the coefficients
lasso_coef = lasso.coef_
print(lasso_coef)
df_columns = df.drop(['fertility', 'Region'], axis=1).columns

# Plot the coefficients
plt.plot(range(len(df_columns)), lasso_coef)
plt.xticks(range(len(df_columns)), df_columns.values, rotation=60)
plt.margins(0.02)
plt.show()


""" Ridge example
# Import necessary modules
from sklearn.linear_model import Ridge
from sklearn.model_selection import cross_val_score

# Setup the array of alphas and lists to store scores
alpha_space = np.logspace(-4, 0, 50)
ridge_scores = []
ridge_scores_std = []

# Create a ridge regressor: ridge
ridge = Ridge(normalize=True)

# Compute scores over range of alphas
for alpha in alpha_space:

    # Specify the alpha value to use: ridge.alpha
    ridge.alpha = alpha
    
    # Perform 10-fold CV: ridge_cv_scores
    ridge_cv_scores = cross_val_score(ridge, X, y, cv=10)
    
    # Append the mean of ridge_cv_scores to ridge_scores
    ridge_scores.append(np.mean(ridge_cv_scores))
    
    # Append the std of ridge_cv_scores to ridge_scores_std
    ridge_scores_std.append(np.std(ridge_cv_scores))

def display_plot(cv_scores, cv_scores_std):
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.plot(alpha_space, cv_scores)

    std_error = cv_scores_std / np.sqrt(10)

    ax.fill_between(alpha_space, cv_scores + std_error, cv_scores - std_error, alpha=0.2)
    ax.set_ylabel('CV Score +/- Std Error')
    ax.set_xlabel('Alpha')
    ax.axhline(np.max(cv_scores), linestyle='--', color='.5')
    ax.set_xlim([alpha_space[0], alpha_space[-1]])
    ax.set_xscale('log')
    plt.show()
    
# Display the plot
display_plot(ridge_scores, ridge_scores_std)

"""