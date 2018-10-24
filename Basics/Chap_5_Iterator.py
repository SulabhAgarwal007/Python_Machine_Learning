# Keywords: iter() - next()
# enumerate() returns an enumerate object that produces a sequence of tuples,
#       and each of the tuples is an index-value pair

# Create a list of strings: mutants
mutants = ['charles xavier',
            'bobby drake',
            'kurt wagner',
            'max eisenhardt',
            'kitty pride']

# Create a list of tuples: mutant_list
mutant_list = list(enumerate(mutants))

# Print the list of tuples
print(mutant_list)

# Unpack and print the tuple pairs
for index1, value1 in enumerate(mutants):
    print(index1, value1)

print("\n Index reset")

# Change the start index
for index2, value2 in enumerate(mutants, start=10):
    print(index2, value2)

# zip() takes any number of iterables and returns a zip object that is an iterator of tuples.
# If you wanted to print the values of a zip object, you can convert it into a list and then print it.
# Printing just a zip object will not return the values unless you unpack it first.

aliases = ['prof x', 'iceman', 'nightcrawler', 'magneto', 'shadowcat']

powers = ['telepathy', 'thermokinesis', 'teleportation', 'magnetokinesis', 'intangibility']

# Create a zip object using the three lists: mutant_zip
mutant_zip = zip(mutants, aliases, powers)

# Print the zip object
print("Type of mutant_zip is {}".format(type(mutant_zip)))
print("Zip: {}".format(mutant_zip))

# Create a list of tuples: mutant_data
mutant_data = list(zip(mutants, aliases, powers))

# Print the list of tuples
print("Type of mutant_data is {}".format(type(mutant_data)))
print(mutant_data)

# Unpack the zip object and print the tuple values
for value1, value2, value3 in mutant_zip:
    print(value1, value2, value3)

# How to unzip? There is no unzip function, but we can use * operator:
# Create a zip object from mutants and powers: z1
z1 = zip(mutants, powers)

# Print the tuples in z1 by unpacking with *
print(zip(*z1))
# Re-create a zip object from mutants and powers: z1
z1 = zip(mutants, powers)

# 'Unzip' the tuples in z1 by unpacking with * and zip(): result1, result2
result1, result2 = zip(*z1)

# Check if unpacked tuples are equivalent to original tuples
print(result1 == mutants)
print(result2 == powers)

## How to read a big data file? Using chunksize parameter can be useful
""""
# Define count_entries()
def count_entries(csv_file, c_size, colname):
#    Return a dictionary with counts of
#    occurrences as value for each key.
    
    # Initialize an empty dictionary: counts_dict
    counts_dict = {}

    # Iterate over the file chunk by chunk
    for chunk in pd.read_csv(csv_file, chunksize=c_size):

        # Iterate over the column in DataFrame
        for entry in chunk[colname]:
            if entry in counts_dict.keys():
                counts_dict[entry] += 1
            else:
                counts_dict[entry] = 1

    # Return counts_dict
    return counts_dict

# Call count_entries(): result_counts
result_counts = count_entries('tweets.csv',10,'lang')

# Print result_counts
print(result_counts)
"""
# List Comprehensions

# Create a 5 x 5 matrix using a list of lists: matrix
matrix = [[col for col in range(5)] for row in range(5)]

# Print the matrix
for row in matrix:
    print(row)
print(matrix)

# Conditions in comprehensions

print("\n Conditions in comprehensions")
print([n**2 for n in range(10) if n % 2 == 0])
print("\n")
print([n**2 if n % 2 == 0 else 0 for n in range(10)])

# Dictionary Comprehensions
print({n: n**2 if n % 2 == 0 else 0 for n in range(10)})

# Generators: using () instead of [] will create a generator. Generator are Lazy evaluations i.e. it does not get
# evaluated until required by the code, hence memory efficient. Generators can be iterated over like a list.
# Generator functions are functions that, like generator expressions, yield a series of values, instead of returning a
# single value. A generator function is defined as you do a regular function, but whenever it generates a value,
# it uses the keyword yield instead of return

# Create a list of strings
lannister = ['cersei', 'jaime', 'tywin', 'tyrion', 'joffrey']

# Define generator function get_lengths
def get_lengths(input_list):
    """Generator function that yields the
    length of the strings in input_list."""
    # Yield the length of a string
    for person in input_list:
        yield len(person)
# Print the values generated by get_lengths()

for value in get_lengths(lannister):
    print(value)


