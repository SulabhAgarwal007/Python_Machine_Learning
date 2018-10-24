import pandas as pd
# Import matplotlib.pyplot
import matplotlib.pyplot as plt

# Read the file into a DataFrame: df
df = pd.read_csv('dob_job_application_filings.csv')

# Print the head of df
# print(df.head())

# Print the tail of df
# print(df.tail())

# Print the shape of df
print(df.shape)

# Print the columns of df
print(df.columns)

# Print the info of df
print(df.info())

# Describe()
print(df.describe()) # this is like summary() in R

# Print the value counts for 'Borough'
print(df['Borough'].value_counts(dropna=False))

# Print the value_counts for 'State'
print(df['State'].value_counts(dropna=False))

# Print the value counts for 'Site Fill'
print(df['Site Fill'].value_counts(dropna=False))

# Plot the histogram, note that plot is pandas function
df['Existing Zoning Sqft'].plot(kind='hist', rot=70, logx=True, logy=True)

# Display the histogram
plt.show()

# Create the boxplot
# df.boxplot(column='Initial Cost', by='Borough', rot=90)

# Display the plot
# plt.show()