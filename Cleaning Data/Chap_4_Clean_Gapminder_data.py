"""
# Downloaded dataset from:
# http://makemeanalyst.com/data-science-with-python/gapminder-dataset/
"""

import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt

gapminder_df = pd.read_csv('gapminder.csv')

def fn_df_info(data_frame):
    print("info:")
    print(data_frame.describe())
    print("\n Columns")
    print(data_frame.columns)
    print("\n head")
    print(data_frame.head())
    return

fn_df_info(gapminder_df)

""" Observations:
There are 16 columns with 213 rows/observations.
Apart from country, rest all should be numeric. Currently it is of object type.
With Assert statement it seems the missing values here are replaced with empty strings.
"""

gapminder_df_updated = gapminder_df #.set_index("country", drop = False)
# print(gapminder_df_updated.head()) # notice the change in index

assert pd.notnull(gapminder_df_updated).all().all()
assert gapminder_df['country'].value_counts().all() == 1

print(gapminder_df_updated.info())

pattern = re.compile('^\s*$') # pattern for empty stringg
print(bool(pattern.match('2.34'))) # testing pattern

for col in gapminder_df_updated.columns:
    if col != 'country':
        gapminder_df_updated[col].replace(pattern, np.nan, regex=True)
        gapminder_df_updated[col] = (
            pd.to_numeric(gapminder_df_updated[col], errors='coerce'))

print(gapminder_df_updated.describe())
plt.clf()
# gapminder_df_updated['incomeperperson'].plot()
# plt.figure()

# gapminder_df_updated.plot(kind = 'scatter', x= 'incomeperperson', y='lifeexpectancy')
# gapminder_df_updated.plot(kind = 'scatter', x= 'incomeperperson', y='co2emissions')

#plt.subplot(2, 1, 1)
plt.hist(np.log(gapminder_df_updated[['incomeperperson']]), bins=10)
plt.xlabel('incomeperperson')
#plt.subplot((2, 1, 2))

# _ = plt.scatter(np.log(gapminder_df_updated[['incomeperperson']]), gapminder_df_updated[['suicideper100th']], label='sucideper100th')

gapminder_df_updated.hist(bins=10, color='steelblue', edgecolor='black', linewidth=1.0, xlabelsize=8, ylabelsize=8, grid=False)

plt.tight_layout(rect=(0, 0, 1.2, 1.2))
plt.show()



