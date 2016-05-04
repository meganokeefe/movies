#using pygal for SVG-formatted plotting
#Each of these methods generates one of my charts
import pygal
from helper_functions import *
import pprint as pp

def sample_bar():
    bar_chart = pygal.Bar()                                            # Then create a bar graph object
    bar_chart.add('Fibonacci', [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55])  # Add some values
    bar_chart.render_to_file('bar_chart.svg')                          # Save the svg to a file


#LGBT films chart
def lgbt_simple_bar():
    line_chart = pygal.Bar()
    line_chart.title = '# of LGBT Films, 1950-2012'
    line_chart.x_labels = map(str, range(1950, 2012))
    #put the list of values here
    counts = [2, 1, 0, 1, 0, 0, 2, 0, 2, 0, 0, 3, 2, 2, 5, 2, 3, 2, 8, 5, 7, 5, 4, 3, 3, 6, 6, 5, 7, 5, 9, 4, 12, 12, 8, 13, 8, 11, 7, 8, 6, 16, 16, 17, 30, 36, 31, 41, 47, 34, 49, 43, 49, 58, 81, 71, 77, 66, 51, 64, 37, 21]
    line_chart.add('LGBT', counts)
    line_chart.render_to_file('lgbt_counts.svg')

def stacked_bar(ditems):
    bar_chart = pygal.StackedBar(x_label_rotation=20, x_labels_major_every=5)
    #get the counts
    drama = get_num_films(diadem, 'Drama', 1970, 2012)
    comedy = get_num_films(diadem, 'Comedy', 1970, 2012)
    action = get_num_films(diadem, 'Action', 1970, 2012)
    romance = get_num_films(diadem, 'Romance Film', 1970, 2012)
    #add to the chart
    bar_chart.title = 'Main Genres Breakdown (Total # Films), 1970-2012'
    bar_chart.x_labels_major = map(str, range(1970, 2012))
    bar_chart.add('Drama', drama)
    bar_chart.add('Comedy', comedy)
    bar_chart.add('Action', action)
    bar_chart.add('Romance', romance)
    bar_chart.render_to_file('fourbar_1970_2012.svg')

#Run from here
diadem = from_pickle('films.pkl')
