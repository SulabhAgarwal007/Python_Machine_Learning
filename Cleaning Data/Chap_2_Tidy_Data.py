"""
For data to be tidy, it must have:
  Each variable as a separate column.
  Each row as a separate observation.

melting a DataFrame using pd.melt(). There are two parameters you should be aware of: id_vars and value_vars.
The id_vars represent the columns of the data you do not want to melt (i.e., keep it in its current shape),
while the value_vars represent the columns you do wish to melt into rows.
By default, if no value_vars are provided, all columns not set in the id_vars will be melted.
This could save a bit of typing, depending on the number of columns that need to be melted.
syntax:
    pd.melt(frame=dataframe, id_vars = [], value_vars =[], var_name = '', value_name = '')

Pivoting data is the opposite of melting it. We can do it using pivot_table()
syntax:
    dataframe.pivot_table(index=[static_col1,..], columns='col_Converetd_tobe', value='value_column')

 by using .pivot_table() and the aggfunc parameter, you can not only reshape your data, but also remove duplicates.
 Finally, you can then flatten the columns of the pivoted DataFrame using .reset_index()

 The default aggregation function used by .pivot_table() is np.mean(). So you could have pivoted the duplicate values
 in this DataFrame even without explicitly specifying the aggfunc parameter.

 Spliting a column with .str function

 # Melt tb: tb_melt
tb_melt = pd.melt(frame=tb, id_vars=['country', 'year'])

# Create the 'gender' column
tb_melt['gender'] = tb_melt.variable.str[0]

# Create the 'age_group' column
tb_melt['age_group'] = tb_melt.variable.str[1:]

# Melt ebola: ebola_melt
ebola_melt = pd.melt(ebola, id_vars=['Date', 'Day'], var_name='type_country',value_name='counts')

# Create the 'str_split' column
ebola_melt['str_split'] = ebola_melt.type_country.str.split('_')

# Create the 'type' column
ebola_melt['type'] = ebola_melt.str_split.str.get(0)

# Create the 'country' column
ebola_melt['country'] = ebola_melt.str_split.str.get(1)

# Print the head of ebola_melt
print(ebola_melt.head())

"""
import pandas as pd

a = "M014"
print(a[0:len(a)])

df = pd.DataFrame(['M0123', 'M3345'])
print(type(df))

print(df.__str__())