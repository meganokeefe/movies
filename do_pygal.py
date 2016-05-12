#using pygal for SVG-formatted plotting
#Each of these methods generates one of my charts
import pygal
from helper_functions import *
import operator
import pprint as pp
from pygal.style import Style

s1 = Style(
 colors=('#EBDF36', '#E8537A', '#E95355', '#E87653', '#E89B53'))

s2 = Style(
 colors=('#ED7E1C', '#E8537A', '#E95355', '#E87653', '#E89B53'))

s3 = Style(
 colors=('#353173', '#E8537A', '#E95355', '#E87653', '#E89B53'))

s4 = Style(
 colors=('#83D4C0', '#E8537A', '#E95355', '#E87653', '#E89B53'))


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

#horizontal bar median revenue chart (between top-occurring genres over all years)
def revenue(ditems):
    whitelist = get_flat_cat_threshold('genres', ditems, 1000)
    with open("genre_revenue_all.txt") as infile:
        raw = infile.readlines()
    cleaned = []
    for r in raw:
        splt = r.split(" ")
        gname = " ".join(splt[:len(splt)-1])
        if gname in whitelist:
            revenueVal = splt[len(splt)-1]
            if revenueVal != 'nan':
                cleaned.append([gname, float(revenueVal)/1000000.0]) #in millions
    cleaned.sort(key=lambda x:-x[1])
    line_chart = pygal.HorizontalBar()
    line_chart.title = 'Median Revenue By Genre (In Millions)'
    for c in cleaned:
        line_chart.add(c[0], c[1])
    line_chart.render_to_file('genre_revenue.svg')


#Run from here
#diadem = from_pickle('films.pkl')
#one_genre(diadem, 'Indie', 1888, 2012, s1)
#revenue(diadem)
