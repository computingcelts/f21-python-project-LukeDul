import cohstats.parser as parser

#################
# Given a metadata and column as arguments, computes the average of the values for a category
# Returns: the average as a float number
#################
def compute_average(data, metadata, column, category) :
    total = 0.0
    count = 1
    for i in  data:


    return total / count

#################
# Given a metadata and column as arguments, computes the standard deviation of the values for a category
# Returns: the standard deviation as a float number
#################

def compute_stdev(data, metadata, column, category) :
    result = 0.0

    # write here your code for this function

    return result

#################
# Given a a metadata and a number (float) as arguments, finds all entries in
# column with values greater than the value passed to the parameter limit
# Returns: A list of strings from the column whose values are greater than limit
#################
def greater_than(data, metadata, column, limit) :
    result = []

    # write here your code for this function

    return result

#################
# Given a a metadata and a number (float) as arguments, finds all entries in
# column with values greater than the value passed to the parameter limit
# Returns: A list of strings from the column whose values are less than limit
#################
def less_than(data, metadata, column, limit) :
    result = []

    # write here your code for this function

    return result
