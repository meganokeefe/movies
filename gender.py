#Megan, 5/9/16
#Code to:
#   1. get the avg. age of male/female actors over time
#   2. for different genres, look at male/female actor breakdown (equity)

from helper_functions import *
from do_pygal import *
import numpy as np

def get_avg_age_year(ditems, gender, year):
    subset = [item for item in ditems if str(year)== item[1]['date'][:4]]
    ages = []
    for film in subset:
        chars = film[1]['chars']
        for c in chars:
            if c[1] == gender:
                if c[3] != '': #some actors don't have ages listed.
                    ages.append(int(c[3])) #append age
    if ages == []:
        return -1
    else:
        return np.mean(ages)

#helper func. returns list of average ages
#gender is 'M' and 'F'
def get_all_ages(ditems, start, end):
    male = []
    female = []
    for year in xrange(start,end):
        print "Getting ", year
        male.append(get_avg_age_year(ditems, 'M', year))
        female.append(get_avg_age_year(ditems, 'F', year))
    print "Male: ", male, "Female", female
    return [male,female]

#age charts
def avg_age_chart(ditems, start, end):
    line_chart = pygal.Line(show_x_labels=False)
    line_chart.title = 'Average Age of Male vs. Female Actors, ' + str(start) + '-' + str(end)
    line_chart.x_labels = map(str, range(start, end))
    #line_chart.add('Firefox', [None, None,    0, 16.6,   25,   31, 36.4, 45.5, 46.3, 42.8, 37.1])
    allAges = get_all_ages(ditems, start, end)
    male = allAges[0]
    female = allAges[1]
    line_chart.add('Male', male)
    line_chart.add('Female', female)
    line_chart.render_to_file('age_'+str(start)+'_'+str(end)+'.svg')

#********************************************

#get male/female ratio for all films in one genre
def get_percent_male(gname, ditems):
    print "Getting percent male for ", gname
    subset = get_by_genre(gname, ditems)
    numFemale = 0.0
    numMale = 0.0
    for film in subset:
        chars = film[1]['chars']
        for c in chars:
            if c[1] == 'F':
                numFemale = numFemale + 1
            if c[1] == 'M':
                numMale = numMale + 1
    print "NUM MALE=", numMale, " and NUM FEMALE=", numFemale
    output = (numMale/(numMale+numFemale))*100.0
    print "PERCENT MALE IS ", output
    return output

#Gender equity chart (M vs. F) for one genre
def genre_gauge(ditems):
    gauge = pygal.SolidGauge(inner_radius=0.70)
    gauge.title = "Percent of Listed Actors that are Male (By Genre), All Years"
    percent_formatter = lambda x: '{:.2g}%'.format(x)
    gauge.value_formatter = percent_formatter

    #add one of these for every genre
    gauge.add('Drama', [{'value': get_percent_male('Drama', ditems), 'maxvalue':100}])
    gauge.add('Comedy', [{'value': get_percent_male('Comedy', ditems), 'maxvalue':100}])
    gauge.add('Rom-Com', [{'value': get_percent_male('Romantic comedy', ditems), 'maxvalue':100}])
    gauge.add('Thriller', [{'value': get_percent_male('Thriller', ditems), 'maxvalue':100}])
    gauge.add('Action/Adventure', [{'value': get_percent_male('Action/Adventure', ditems), 'maxvalue':100}])
    gauge.add('Animation', [{'value': get_percent_male('Animation', ditems), 'maxvalue':100}])
    gauge.add('Indie', [{'value': get_percent_male('Indie', ditems), 'maxvalue':100}])
    gauge.add('Sports', [{'value': get_percent_male('Sports', ditems), 'maxvalue':100}])
    gauge.add('LGBT', [{'value': get_percent_male('LGBT', ditems), 'maxvalue':100}])


    gauge.render_to_file('ninegauge.svg')

print "Reading data.."
diadem = from_pickle('films.pkl')
#print "Generating age chart..."
#avg_age_chart(diadem, 1930, 2012)

genre_gauge(diadem)
