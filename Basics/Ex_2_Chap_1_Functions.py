# Functions - Single value parameter
def square(x) :
    return x **2

print(square(2))


# Define shout_all with parameters word1 and word2
def shout_all(word1, word2):
    # Concatenate word1 with '!!!': shout1
    shout1 = word1 + '!!!'

    # Concatenate word2 with '!!!': shout2
    shout2 = word2 + '!!!'

    # Construct a tuple with shout1 and shout2: shout_words
    shout_words = (shout1, shout2)

    # Return shout_words
    return shout_words


# Pass 'congratulations' and 'you' to shout_all(): yell1, yell2
yell1, yell2 = shout_all('congratulations', 'you')

# Print yell1 and yell2
print(yell1)
print(yell2)

""""
# Define count_entries()
def count_entries(df, col_name):
    #r eturn a dictionary with counts of
    occurrences as value for each key.

    # Initialize an empty dictionary: langs_count
    langs_count = {}

    # Extract column from DataFrame: col
    col = df[col_name]

    # Iterate over lang column in DataFrame
    for entry in col:

        # If the language is in langs_count, add 1
        if entry in langs_count.keys():
            langs_count[entry] += 1
        # Else add the language to langs_count, set the value to 1
        else:
            langs_count[entry] = 1

    # Return the langs_count dictionary
    return langs_count

# Call count_entries(): result
result = count_entries(tweets_df, 'lang')

# Print the result
print(result)

"""

# use nonlocal keyword to refer a variable from outside scope of a function

# #Function with variable-length arguments (*args), (**kwargs)
# Flexible arguments enable you to pass a variable number of arguments to a function.

"""
# Define report_status
def report_status(**kwargs):
    #  Print out the status of a movie character.

    print("\nBEGIN: REPORT\n")

    # Iterate over the key-value pairs of kwargs
    for key, value in kwargs.items():
        # Print out the keys and values, separated by a colon ':'
        print(key + ": " + value)

    print("\nEND REPORT")

# First call to report_status()
report_status(name="luke", affiliation="jedi",status="missing")

# Second call to report_status()
report_status(name="anakin", affiliation="sith lord", status="deceased")

"""

# Lambda Functions:The best use case for lambda functions, however, are for when you want these simple functionalities
# to be anonymously embedded within larger expressions. What that means is that the functionality is not stored in the
# environment, unlike a function defined with def. To understand this idea better, you will use a lambda function in
# the context of the map() function.

"""
# Create a list of strings: spells
spells = ["protego", "accio", "expecto patronum", "legilimens"]

# Use map() to apply a lambda function over spells: shout_spells
shout_spells = map(lambda item: item + '!!!', spells)

# Convert shout_spells to a list: shout_spells_list
shout_spells_list = list(shout_spells)

# Convert shout_spells into a list and print it
print(shout_spells_list)

"""

# usage of lambda function with map(), filter() and reduce() functions