import cohstats.parser as parser
import math


#################
# Given a metadata and column as arguments, computes the average of the values for a category
# Returns: the average as a float number
# print(stats.compute_average(parser.city_counts, 'day_of_week', 'division', '311 Call Handling'))
# In english: compute the average of the 'day_of_week' values that
# are on the same line as all of the '311 Call Handling' values.
#
#################
# print(stats.compute_average(parser.city_data, 'day_of_week', 'division', '311 Call Handling'))
def compute_average(data, metadata, column, category): # note that metadata refers to the integer and column refers to the division or category
    total = 0.0
    count = 0
    indexer = 0
    if (column == metadata) and (category == metadata):
        for n in data[metadata]:
            count += 1
            total += n
        return total / count

    else:
        for z in data:
            if z == column:
                for i in data[z]:  # 'division'
                    indexer += 1
                    if i == category:  # '311 Call Handling'
                        counter = 1
                        for h in data[metadata]:
                            if indexer == counter:
                                total += h
                                count += 1
                            counter += 1
    return total / count


#################
# Given a metadata and column as arguments, computes the standard deviation of the values for a category
# Returns: the standard deviation as a float number
#################

def compute_stdev(data, metadata, column, category): # note that metadata refers to the integer and column refers to the division or category
    result = 0.0
    average = compute_average(data, metadata, column, category)
    # print(average)
    total = 0.0
    count = 0
    sum = 0
    indexer = 0

    if (column == metadata) and (category == metadata):
        for h in data[metadata]:
            sum += ((h - average) ** 2)
            total += h
            count += 1
        result = math.sqrt(sum / (count - 1))

    else:
        for z in data:
            if z == column:
                # print(z)
                for i in data[z]:  # 'division'
                    indexer += 1
                    if i == category:  # '311 Call Handling'
                        # print('INDEX:', indexer)
                        counter = 1
                        for h in data[metadata]:
                            if indexer == counter:
                                # print('Variance', h - average)
                                # print('Squared', (h - average)**2)
                                sum += ((h - average) ** 2)
                                # print('Sum: ', sum)
                                total += h
                                count += 1
                            counter += 1
        result = math.sqrt(sum / (count - 1))

    return result


#################
# Given a metadata and a number (float) as arguments, finds all entries in
# column with values greater than the value passed to the parameter limit
# Returns: A list of strings from the column whose values are greater than limit

# print(stats.greater_than(parser.city_counts, 'division', 4))
#################
# source: https://stackoverflow.com/questions/12897374/get-unique-values-from-a-list-in-python
def greater_than(data, metadata, limit):  # column is redundant
    result = []
    unique = {}
    for n in data[metadata]:
        if n not in unique:
            unique[n] = 0
    # print(unique)

    count = 0
    for n in unique:
        for i in data[metadata]:
            if i == n:
                count += 1

        unique[n] = count
        count = 0

    for x, y in unique.items():
        if y > limit:
            result.append(x)
    # print(unique)
    return result


#################
# Given a a metadata and a number (float) as arguments, finds all entries in
# column with values greater than the value passed to the parameter limit
# Returns: A list of strings from the column whose values are less than limit
#################
def less_than(data, metadata, limit):
    result = []
    unique = {}
    for n in data[metadata]:
        if n not in unique:
            unique[n] = 0
    # print(unique)

    count = 0
    for n in unique:
        for i in data[metadata]:
            if i == n:
                count += 1
        unique[n] = count
        count = 0

    for x, y in unique.items():
        if y < limit:
            result.append(x)
    # print(unique)
    return result
