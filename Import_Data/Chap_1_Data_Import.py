import os

print("Path at terminal when executing this file")
print(os.getcwd() + "\n")
print(os.listdir(os.getcwd()))
"""
print("This file path, relative to os.getcwd()")
print(__file__ + "\n")

print("This file full path (following symlinks)")
full_path = os.path.realpath(__file__)
print(full_path + "\n")

print("This file directory and name")
path, filename = os.path.split(full_path)
print(path + ' --> ' + filename + "\n")

print("This file directory only")
print(os.path.dirname(full_path))
"""

# Reading local text file
filename = 'labels.txt'
file_s = open(filename, mode='r')
text = file_s.read()
print(text)
file_s.close()

# context manager: without explicitly closing the file, it remains open for the context only

with open('labels.txt', mode='r') as file_s:
    print(file_s.readline())
    print(file_s.readline())

# Zen of Python: these are aphorism (principles)
# import this

# Loading CSV file
# MNIST: A hand written dataset for image processing trainings. Here Numpy is usefull as it is fast, but it does not
# work with dataset having multiple data types.
import numpy as np
import matplotlib.pyplot as plt

file_csv = 'mnist_test_MNIST.csv'
data_csv = np.loadtxt(file_csv, delimiter=',')
# print(data_csv[1, :])
# im = data_csv[21, 1:]
# im_sq = np.reshape(im, (28, 28))

# Plot reshaped data (matplotlib.pyplot already loaded as plt)
# plt.imshow(im_sq, cmap='Greys', interpolation='nearest')
# plt.show()

"""
There are a number of arguments that np.loadtxt() takes that you'll find useful: delimiter changes the delimiter that 
loadtxt() is expecting, for example, you can use ',' and '\t' for comma-delimited and tab-delimited respectively; 
skiprows allows you to specify how many rows (not indices) you wish to skip; usecols takes a list of the indices of the 
columns you wish to keep.
"""

# To import data with multiple datatypes we can use np.genfromtxt() or np.recfromcsv() instead of np.loadtxt()

# below code is not working bcz underlying file as some encoding
"""
file_csv_m_data_type = 'Most-Recent-Cohorts-Scorecard-Elements.csv'
data_csv_m_data_type = np.recfromcsv(file_csv_m_data_type)
np.shape(data_csv_m_data_type)

"""

import pandas as pd

file_pd_csv = pd.read_csv('Most-Recent-Cohorts-Scorecard-Elements.csv')
file_pd_csv.info()
print(file_pd_csv.head())

# another example pd.read_csv(file, sep='\t', comment='#', na_values='Nothing')

"""
There are a number of datatypes that cannot be saved easily to flat files, such as lists and dictionaries. If you want 
your files to be human readable, you may want to save them as text files in a clever manner. JSONs are appropriate for 
Python dictionaries. However, if you merely want to be able to import them into Python, you can serialize them. 
All this means is converting the object into a sequence of bytes, or a bytestream.

# Import pickle package
import pickle

# Open pickle file and load data: d
with open('data.pkl', 'rb') as file:  # replace data.pkl with some correct data set.
    d = pickle.load(file)

# Print d
print(d)

# Print datatype of d
print(type(d))

# Importing Excel Sheet

# Assign spreadsheet filename: file
file = 'battledeath.xlsx'

# Load spreadsheet: xl
xl = pd.ExcelFile(file)

# Print sheet names
print(xl.sheet_names)

# Load a sheet into a DataFrame by name: df1
df1 = xl.parse('2004')

# Print the head of the DataFrame df1
print(df1.head())

# Load a sheet into a DataFrame by index: df2
df2 = xl.parse(0)

# Print the head of the DataFrame df2
print(df2.head())

# Parse the first sheet and rename the columns: df1
df1 = xl.parse(0, skiprows=[0], names=['Country', 'AAM due to War (2002)']) # check that all parameters are of List type

# Print the head of the DataFrame df1
print(df1.head())

# SAS and Stata file loading

############################SAS#############
# Import sas7bdat package
from sas7bdat import SAS7BDAT

# Save file to a DataFrame: df_sas
with SAS7BDAT('sales.sas7bdat') as file:
    df_sas = file.to_data_frame()

# Print head of DataFrame
print(df_sas.head())

# Plot histogram of DataFrame features (pandas and pyplot already imported)
pd.DataFrame.hist(df_sas[['P']])
plt.ylabel('count')
plt.show()

#########################Stata############
# Import pandas
import pandas as pd

# Load Stata file into a pandas DataFrame: df
df = pd.read_stata('disarea.dta')

# Print the head of the DataFrame df
print(df.head())

# Plot histogram of one column of the DataFrame
pd.DataFrame.hist(df[['disa10']])
plt.xlabel('Extent of disease')
plt.ylabel('Number of coutries')
plt.show()

###################HDF5########
# HDF5 - Hierarchical Data Format Version 5, while accessing such files in Python treat them as Key-Value pair
# Import packages
import numpy as np
import h5py

# Assign filename: file
file = 'LIGO_data.hdf5'

# Load file: data
data = h5py.File(file, 'r')

# Print the datatype of the loaded file
print(type(data))

# Print the keys of the file
for key in data.keys():
    print(key)

# Get the HDF5 group: group
group = data['strain']

# Check out keys of group
for key in group.keys():
    print(key)

# Set variable equal to time series data: strain
strain = data['strain']['Strain'].value

# Set number of time points to sample: num_samples
num_samples = 10000

# Set time vector
time = np.arange(0, 1, 1/num_samples)

# Plot data
plt.plot(time, strain[:num_samples])
plt.xlabel('GPS Time (s)')
plt.ylabel('strain')
plt.show()

########################MATLAB File#################
# Import package
import scipy.io

# Load MATLAB file: mat
mat = scipy.io.loadmat('albeck_gene_expression.mat')

# Print the datatype type of mat
print(type(mat))

"""