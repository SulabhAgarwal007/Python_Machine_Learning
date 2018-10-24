# Dictionary syntax dict = {Key: Value}

""""
countries = ['spain', 'france', 'germany', 'norway']
capitals = ['madrid', 'paris', 'berlin', 'oslo']

# From string in countries and capitals, create dictionary europe

europe = {
    "spain":"madrid",
    "france":"paris",
    "germany":"berlin",
    "norway":"oslo"
}
# Print europe
print(europe)

# Print out the keys in europe
print(europe.keys())

# Print out value that belongs to key 'norway'
print(europe['norway'])

# Add italy to europe
europe["italy"] = "rome"

# Print out italy in europe
print('italy' in europe)

# Add poland to europe
europe["poland"] = "warsaw"

# Print europe
print(europe)

# Did you notice that the order of the printout is not the same as the order in the dictionary's definition?
# That's because dictionaries are inherently unordered.
# Dictionary of dictionaries
europe = { 'spain': { 'capital':'madrid', 'population':46.77 },
           'france': { 'capital':'paris', 'population':66.03 },
           'germany': { 'capital':'berlin', 'population':80.62 },
           'norway': { 'capital':'oslo', 'population':5.084 } }


# Print out the capital of France
print(europe['france']['capital'])

# Create sub-dictionary data
data = {'capital':'rome', 'population':59.83}

# Add data to europe under key 'italy'
europe['italy'] = data

# Print europe
print(europe)

"""

###################
# Pandas package: Pandas is an open source library, providing high-performance,
# easy-to-use data structures and data analysis tools for Python. The DataFrame is one of Pandas' most
# important data structures. It's basically a way to store tabular data where you can label the rows and the columns.
# One way to build a DataFrame is from a dictionary.

# Pre-defined lists
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr = [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]


# Import pandas as pd
import pandas as pd

# Create dictionary my_dict with three key:value pairs: my_dict
my_dict = {'country': names, 'drives_right': dr, 'cars_per_cap': cpc}

# Build a DataFrame cars from my_dict: cars

cars = pd.DataFrame(my_dict)
# Print cars
print(cars)

# In above output the row labels (i.e. the labels for the different observations) were automatically
# set to integers from 0 up to 6. To solve this we define row labels

# Definition of row_labels
row_labels = ['US', 'AUS', 'JAP', 'IN', 'RU', 'MOR', 'EG']

# Specify row labels of cars
cars.index = row_labels

# Print cars again
print(cars)

# print(dir())

FL_insurance_sample = pd.read_csv('FL_insurance_sample.csv', index_col=0)

# single squared bracket gives data type as Panda Series, while double squared brackets gives data frame.

print(FL_insurance_sample[['statecode', 'county']].head()) # squared bracket column access
print(FL_insurance_sample[1:3]) # squared bracket row access

# Using loc() to restrict the selection
print(FL_insurance_sample.loc[[119736, 206893]][["statecode", "county"]])

# Using iloc() for same purpose
print(FL_insurance_sample.iloc[[2, 3], [3, 4]])

# Comparision in dataframes
print("\n Data Frame comparision demo\n")
europe_dict = {'spain': {'capital': 'madrid', 'population': 46.77}, 'france': {'capital': 'paris', 'population': 66.03}, 'germany': {'capital': 'berlin', 'population': 80.62}, 'norway': {'capital': 'oslo', 'population': 5.084}}

europe_df = pd.DataFrame(europe_dict)
print(europe_df)
temp = europe_df.loc['population'] > 50
# remember logical operation are to be performed on Panda Series and not on Panda DataFrame

# E.g. To get countries with population > 50
# print(europe_df[[temp, temp]])






