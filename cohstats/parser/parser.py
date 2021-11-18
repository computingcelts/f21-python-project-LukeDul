import string

# city_data is a variable of type dictionary, where each element is a key : value pair,
# the key is an integer representing the line number in the text file; the value of each key
# is a list containing the values read from the text file. Note that when building the dictionary some values
# have to be converted into integer.
input_data = {}

# city_data is a variable of type dictionary, where each element is a key : value pair,
# the key is one of the 13 metadata; the value of each key is a list containing the
# values read from the text file. Note that when building the dictionary some values
# have to be converted into integer.
city_data = {}

# city_counts is a variable of type dictionary (a nested dictionary), where the key is
# one of 10 metadata (day_of_week, hour_of_day, neighborhood, district, division,
# serv_type, queue, wait, days, origin). The value is another dictionary;
# where the key is a unique information from the dataset for that metadata and
# its corresponding value is a count of how many times, that information appears
# in the dataset.
city_counts = {}

# city_stats is a variable of type dictionary (a nested dictionary), where the key is
# one of only 4 metadata: 'day_of_week', 'hour_of_day', 'wait', 'days'; the value is
# another dictionary; where the keys are: 'avg', 'stdev', 'var', and their
# corresponding values will be computed by invoking functions defined in the stats module
city_stats = {}

# reads from a text file in disk and stores its content in a dictionary
# DON'T MODIFY THIS FUNCTION
def read_file(file) :
    list_of_lines = {}

    print('input file is: ' + file)

    with open('data/' + file) as f:
        count = 1
        for line in f:
            if count > 1 :
                values_in_line = line.replace('\n','').split('|')
                # replaces the third element in the list with its corresponding
                # value as integer
                values_in_line[2] = int(values_in_line[2])
                list_of_lines[count-1] = values_in_line
            count += 1

    print('read a total of ', count ,' lines from file: ', file)
    # returns a list with  all lines read from the input file
    return list_of_lines

# city_data is a variable of type dictionary,
#   where each element is a key : value pair,
#         the key is one of the 13 metadata;
#         the value of each key is a list containing the values read from the text file.
#         Note that when building the dictionary some values have to be converted into integer.
#
# LIST OF KEYWORDS REQUIRED
# date|time|day_of_week|hour_of_day|neighborhood|key_map|district|division|serv_type|queue|wait|days|origin
#
# EXAMPLE OF POPULATED DICTIONARY
# city_data = { 'date':
#                      [ '2016-08-23', '2016-08-22', '2016-10-20', . . .] ,
#               'time' :
#                       [ '20:40:25', '20:28:14', '12:47:28', . . .] ,
#               'day_of_week' :
#                       [ 2, 1, 4, . . .] ,
#               'hour_of_day' :
#                       [ 20, 20, 12, . . .] ,
#               'neighborhood' :
#                       [ 'SPRING BRANCH CENTRAL', 'MIDTOWN', 'INDEPENDENCE HEIGHTS', . . .] ,
# ...

# invoke this function in your test script to build the city_data dictionary
# this function has to be invoked only once in your entire code
def builds_city_data(data) : # argument will be parser.input_data
    data_processed = {
        'date': [],
        'time': [],
        'day_of_week': [],
        'hour_of_day': [],
        'neighborhood': [],
        'key_map': [],
        'district': [],
        'division': [],
        'serv_type': [],
        'queue': [],
        'wait': [],
        'days': [],
        'origin': [],
    }

    list_length = 0
    for n in data:
         list_length += 1

    # for n in range(1, list_length+1, 13):
    #     for i in range(1, 14)
    #
    data_processed['date'].append(data[[n]])



    return data_processed

# invoke this function in your test script to build the city_counts dictionary
# this function has to be invoked only once in your entire code
def builds_city_counts(data) :
    data_processed = {}

    return data_processed

# invoke this function in your test script to build the city_stats dictionary
# this function has to be invoked only once in your entire code
def builds_city_stats(data) :
    data_processed = {}

    return data_processed