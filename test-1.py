# USE THIS SCRIPT BY MEMBER "A" OF YOUR TEAM TO TEST THE CODE
# AKA Luke's test script
import turtle
import cohstats as cs
import cohstats.stats as stats
import cohstats.parser as parser
import cohstats.graphics as graphics
import pprint

def main():
    print('***************************************************')
    print('building dictionaries')
    print('***************************************************')
    # builds dictionary with documents and words in each document
    # use this for testing
    parser.input_data = cs.parser.read_file('coh_311_data.csv')
    #pprint.pprint(parser.input_data, width=1)

    # using the dictionary built in the previous step, builds a new dictionary
    parser.city_data = parser.builds_city_data(parser.input_data)  # FINISHED
    pprint.pprint(parser.city_data, width=1)

    # using a previously created dictionary, builds a new dictionary
    parser.city_counts = parser.builds_city_counts(parser.city_data)  # FINISHED
    #pprint.pprint(parser.city_counts, width=1)

    # using a previously created dictionary, builds a new dictionary
    parser.city_stats = parser.builds_city_stats(parser.input_data)  # INCOMPLETE FINISH AFTER STATS IS DONE
    pprint.pprint(parser.city_stats, width=1)

    print('***************************************************')
    print('computing stats')
    print('***************************************************')

    # You have to implement the functions in stats, then depending on what information
    # dictionaries you built before, you have to decide which one to pass as
    # argument.
    # In this examples the parser.city_counts has to be replace with the container you believe is the
    # best suited to compute that statistic
    print(stats.compute_average(parser.city_data, 'wait', 'queue', '311_Seniors'))
    print(stats.compute_stdev(parser.city_counts, 'day_of_week', 'division', '311 Call Handling'))
    print(stats.greater_than(parser.city_counts, 'day_of_week', 'division', 4))
    print(stats.less_than(parser.city_counts, 'day_of_week', 'division', 2))

    print('***************************************************')
    print('graphics')
    print('***************************************************')

    # these are some plain examples on how to draw graphics on the screen using the turtle graphics package
    graphics.draw_text('Click anywhere on the window to close turtle graphics', 10, 10)
    graphics.draw_bar(5, 50, 200, 5, 'blue')
    graphics.draw_bars(20, 50, 'red', total_bars = 5)

    graphics.draw_text('These are some examples on how to use turtle graphics', 10, 550)

    # these are examples on how to invoke the graphics functions, you have to change the first argument
    # to pass a dictionary already built in the previous steps
    graphics.plot_top_k_service_types(parser.city_counts, 'day_of_week', 10)
    graphics.plot_bottom_k_service_types(parser.city_counts, 'day_of_week', 10)
    graphics.plot_service_by_day(parser.city_counts, 1)
    graphics.plot_service_by_hour(parser.city_counts, 11)

    # makes the the plot stop, comment this line when working on your code
    #graphics.render()

main()