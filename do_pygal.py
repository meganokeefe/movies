#using pygal for SVG-formatted plotting
#Each of these methods generates one of my charts
import pygal
from helper_functions import *
import pprint as pp
from pygal.style import Style

bw_style = Style(
 colors=('#000000', '#E8537A', '#E95355', '#E87653', '#E89B53'))

brown_style = Style(
 colors=('#b8603a', '#E8537A', '#E95355', '#E87653', '#E89B53'))

lime_style = Style(
 colors=('#85f63d', '#E8537A', '#E95355', '#E87653', '#E89B53'))

def sample_bar():
    bar_chart = pygal.Bar()                                            # Then create a bar graph object
    bar_chart.add('Fibonacci', [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55])  # Add some values
    bar_chart.render_to_file('bar_chart.svg')                          # Save the svg to a file

#LGBT films chart
def one_genre(ditems, gname, start, end, pstyle):
    line_chart = pygal.Bar(x_label_rotation=30, x_labels_major_every=5, style=pstyle)
    line_chart.title = "Number of " + gname + " films, " + str(start) + "-" + str(end)
    line_chart.x_labels = map(str, range(start, end))
    #put the list of values here
    counts = get_num_films(ditems, gname, start, end)
    line_chart.add(gname, counts)
    line_chart.render_to_file("out/"+gname+"_counts_"+str(start)+"_"+str(end)+'.svg')

def stacked_bar(ditems):
    bar_chart = pygal.StackedBar(x_label_rotation=20, x_labels_major_every=5)
    #get the percentages
    drama = get_num_films(diadem, 'Drama', 1970, 2012)
    comedy = get_num_films(diadem, 'Comedy', 1970, 2012)
    action = get_num_films(diadem, 'Action', 1970, 2012)
    romance = get_num_films(diadem, 'Romance Film', 1970, 2012)
    #add to the chart
    bar_chart.title = 'Main Genres Breakdown (Percent of Films), 1970-2012'
    bar_chart.x_labels_major = map(str, range(1970, 2012))
    bar_chart.add('Drama', drama)
    bar_chart.add('Comedy', comedy)
    bar_chart.add('Action', action)
    bar_chart.add('Romance', romance)
    bar_chart.render_to_file('fourbar_1970_2012.svg')

#Run from here
diadem = from_pickle('films.pkl')
#one_genre(diadem, 'Black-and-white', 1888, 2012, bw_style)
#one_genre(diadem, 'Western', 1888, 2012, brown_style)
#one_genre(diadem, 'Science Fiction', 1910, 2012, lime_style)
