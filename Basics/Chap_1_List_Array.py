
print("Hello Sulabh!")

# Variable

Hieght = 1.45
Weight = 1.56

BMI = Weight / Hieght ** 2

print(BMI)
print(type(BMI))

# int(), float(), str(), bool() --functions for conversion
print("error demo for String + int " + str(1 + 2))  # here int and str cannot be put together, hence str() is used.
print("error demo for String + int {}".format(1 + 2)) # alternative of above

# List example : List are Mutable.

a = ["a", 1, "b", 2, "c", 3];
print(a[2:4])  # not a[4] is not the part of the output. behaviour is "inclusive":"exclusive"

b = [["a", 1], ["b", 2], ["c", 3]];
print(b[2][0])  # output 1st element in 3rd list
print(b[2])  # output 3rd list

c = b  # + [["d", 4]]; here without list() or any other list operation, c is just a pointer to b
x = list(c)
print("c: {}".format(c))
del (c[1:2]);  # other methods to delete an element are pop(), remove()
print("c" + str(c))
# it seems del() function does not create a new list, instead it will append the existing one.
print("b" + str(b))
print("x" + str(x))
# Imp: check the output above after removing "+ [["d", 4]]" from the definition of c. The output of b and c will result
# into same output as they both refer to the same list in memory. hence to create a new list either ues list(b) or b[:]

# Functions
# print, len, sorted, help
# Methods: everything in Python is objects like int, float, string, list, bool and each object has it's specific
# functions called methods.for e.g.
print(BMI.__abs__())
# some methods do not change the content of the objects, while some do. like upper and append.
s = 'spam-spam-spam'
delimiter = '-'
print(type(s.split(delimiter)))  # sting operations resulting into list
# join() is inverse of split() function

# Identical and equivalent: If 2 objects are identical then they are equivalent, but reverse may not be true
a = 'banana'; b = 'banana'; print('Identical: {}'.format(a is b))
a = [1, 2, 3]; b = [1, 2, 3];print('Equivalent: {}'.format(a is b))

# Package - goto file>settings>project interpreter>add to browse and install the package.
import numpy as np

print(type(np.array([1, 2, 3, 4])))

# suppose we need only Array() from numpy package, then we do not need to import whole package, instead below will work
# from numpy import array

# List vs Numpy.Array - we cannot perform general calculation on List for element wise, while this is doable with Array
# Array is much faster than list.
# numpy arrays cannot contain elements with different types. If you try to build such a list, some of the elements'
# types are changed to end up with a homogeneous list. This is known as type coercion.

my_list = [1, 2, 3, 4]
my_array = np.array(my_list)  # type: ndarray

print(my_list + my_list)
print(my_array + my_array)

# multi-dimensional array in numoy
n_dim_array = np.array(([34, 45, 23, 56, 43],
                        [21, 34, 98, 56, 67]))

var = n_dim_array.shape  # type: tuple
print("Multidimensional Array Size: " + str(var))
print(n_dim_array[:, 1])
print(n_dim_array[0][3] == n_dim_array[1][3])

print("Average: "+str(np.mean(n_dim_array[:, 0])))

height = np.round(np.random.normal(1.45, 0.2, 100), 2)  # here 1.45 is loc or mean, 0.2 is scale or standard deviation
print(height < 1.1) # this gives the boolean output
print(height[height > 1.40]) # this gives the output as of correct index

# other stats functions - np.median, np.std, np.corrcoef(col1, col2)

# logical and, or and not does not work with arrays
# hence we have to use logical_or(), logical_and() and logical_not() functions

## Loops
# Initialize offset
offset = -6

# Code the while loop
while offset != 0 :
    print("correcting...")
    if offset > 0:
        offset = offset - 1
    else:
        offset = offset + 1
    print(offset)

# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Change for loop to use enumerate()
for x, y in enumerate(areas): # enumerate() function is used to return the index and value from a list.
    print("room {}: {}".format(x, y))
# house list of lists
house = [["hallway", 11.25],
             ["kitchen", 18.0],
             ["living room", 20.0],
             ["bedroom", 10.75],
             ["bathroom", 9.50]]

# Build a for loop from scratch
for x, y in house:
    print("the {} is {} sqm".format(x, y))

# Definition of dictionary , notice the items() function
europe_demo = {'spain': 'madrid', 'france': 'paris', 'germany': 'berlin',
                  'norway': 'oslo', 'italy': 'rome', 'poland': 'warsaw', 'austria': 'vienna'}

# Iterate over europe
for x, y in europe_demo.items():
    print("the capital of {} is {}".format(x, y))

# for looping over 2D Array elements, use np.nditer(Array_Name)

# Looping over DataFrame: Iterating over a Pandas DataFrame is typically done with the iterrows() method.
# Used in a for loop, every observation is iterated over and on every iteration the row label
# and actual row contents are available. for e.g.
# Adapt for loop
# for lab, row in cars.iterrows() :
#    print("{}: {}".format(lab, row['cars_per_cap']))

# # Use .apply(str.upper) -- this does not need a loop for iterating over the items, hence efficient.
# cars["COUNTRY"] = cars["country"].apply(str.upper)
#
# print(cars)

