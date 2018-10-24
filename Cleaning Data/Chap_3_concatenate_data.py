"""
concat() in pandas does a row wise concatenation by default (attribute axis =0) and does not reset row index by default
syntax:
# Concatenate uber1, uber2, and uber3: row_concat
row_concat = pd.concat([uber1,uber2,uber3])

for column wise concatenation pass axis=1 as parameter.
# Concatenate ebola_melt and status_country column-wise: ebola_tidy
ebola_tidy = pd.concat([ebola_melt, status_country], axis=1)

In case we have to combine multiple files, then we can use globbing. Globbing is searching for file pattern and then
creating a list of all the files. Wildcards like *, ? work with glob function
example
# Import necessary modules
import pandas as pd
import glob

# Write the pattern: pattern
pattern = '*.csv'

# Save all file matches: csv_files
csv_files = glob.glob(pattern)

# Load the second file into a DataFrame: csv2
csv2 = pd.read_csv(csv_files[1])

Merging data allows you to combine disparate datasets into a single dataset to do more complex analysis.
# Merge the DataFrames: o2o
o2o = pd.merge(left=site, right=visited, left_on='name', right_on='site')

the 1-to-1 correspondence between the name column of the site DataFrame and the site column of the visited DataFrame.
This is what made the 1-to-1 merge possible.

## Datatype conversion
Converting Datatypes can reduce the size of dataset, hence inportant. especially the categorical variables.

Syntax: df.column.astype('category')

Similarly to convert object type into numeric:
    pd.to_numeric(df['column'], error='coerce')
Here, 'coerce' keyword is to convert any non-numeric value into proper NaN.

Using Regular Expression we can use 're' package
for e.g. to search any pattern for $1234.45 this could be searched by: ^\$\d*\.\d{2}$
Here,
    ^  - start of a pattern
    \$ - escape char + $
    \d*- any number of integers
    \. - escape char + .
    \d{2}- 2 digits only
    $ - signifying end of pattern

with re package we can use var = re.compile('pattern') and var.match('sample string') to test our pattern.
"""
import numpy as np
import pandas as pd
import re

prog = re.compile('\d*')

print(bool(prog.match('this is 1st regex tester 2223')))

# Find the numeric values: matches. Note the '+' symbol here, that the previous element is matched one or more times.
# This ensures that 10 is viewed as one number and not as 1 and 0.
matches = re.findall('\d+', 'the recipe calls for 10 strawberries and 1 banana')

# Print the matches
print(matches)

# Write the second pattern
pattern2 = bool(re.match(pattern='\$\d*\.\d{2}', string='$123.45'))
print(pattern2)

# Write the third pattern
pattern3 = bool(re.match(pattern='[A-Z]\w*', string='Australia'))
print(pattern3)

# Write the regular expression: pattern "to be tested"
pattern = '^[A-Za-z\.\s]*$'

# Apply function can be used to re-iteratively apply a function over each row of  dataset

# here's a function that squares a variable used in an .apply() method:
def my_square(x):
    return x ** 2

df = pd.DataFrame([1,2,3,45])

print(df.apply(my_square))


# The equivalent code using a lambda function is:
print(df.apply(lambda x: x ** 2))

"""
# Write the lambda function using replace
tips['total_dollar_replace'] = tips['total_dollar'].apply(lambda x: x.replace('$', ''))

# Write the lambda function using regular expressions
tips['total_dollar_re'] = tips['total_dollar'].apply(lambda x: re.findall('\d+\.\d+', x)[0])
"""

# df.drop_duplicates() function drop duplicate rows from a data frame. We can use fillna() function to fill
# missing values.

"""
# Calculate the mean of the Ozone column: oz_mean
oz_mean = airquality['Ozone'].mean()

# Replace all the missing values in the Ozone column with the mean
airquality['Ozone'] = airquality['Ozone'].fillna(oz_mean)

# Print the info of airquality
print(airquality.info())
"""

# Use Assert statement to programmatically check for missing values and to confirm that all values are positive.
# The first .all() method will return a True or False for each column, while the second .all()
# method will return a single True or False.
"""
# Assert that there are no missing values
assert pd.notnull(ebola).all().all()

# Assert that all values are >= 0
assert (ebola>=0).all().all()
"""