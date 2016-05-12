# Exploring the CMU Movies Corpus 
Final project for CS249, Spring 2016

Megan O'Keefe, 5/11/16

### Links
Original data source: [http://www.cs.cmu.edu/~ark/personas/
](http://www.cs.cmu.edu/~ark/personas/)

My re-formatted pickle file, combining the movie metadata, character metadata, and summaries (132MB): 
[Google Drive](https://drive.google.com/file/d/0BzuUXoRjB9NreUhkQ0YxMFdGSHM/view?usp=sharing )

Webpage with my charts and findings: [http://cs.wellesley.edu/~mokeefe2/cs249/movies
](http://cs.wellesley.edu/~mokeefe2/cs249/movies)

My genre explorer: [cs.wellesley.edu/~mokeefe2/cs249/genres](cs.wellesley.edu/~mokeefe2/cs249/genres)

![image](genre_explorer.jpg)

`stopwords.txt` taken from: [http://www.ranks.nl/stopwords ](http://www.ranks.nl/stopwords)


### Project Description and Goals 
For my final project, I sought to do an exploratory, end-to-end data analysis of the Carnegie Mellon Movies corpus. This dataset contains ~80,000 films since 1888 and their metadata, along with plot summaries for roughly half those films. The dataset also contains information about the characters within each film (eg. gender, age). My main learning goal for this project was to improve my data wrangling and visualization skills, and to practice them extensively on a brand-new dataset. I also wanted to learn visualizations with Pygal for the first time. Pygal's interactive SVGs have the added benefit of easy embedding in an HTML page, which I knew I would need for the end of the project. 


### Process 
(Following the steps of the data science cycle)
#### 1. Ask Interesting Questions
I went into this project with four specific areas of analysis:

1. What is the relationship between **genre and box office revenue**? Which genres make the most money, on average?
2. Some films are listed as having more than one genre. What are the most common **intersections between genres** (genre co-occurrence)?
3. What is the average age of **the male vs. female film actor** over time? What is the ratio between male/female actors across different genres? Are there any genres in which women dominate men?
4. Which words and phrases in the **plot summaries** are correlated with top-selling blockbuster films?

#### 2. Get the Data
Given that this data is very text-heavy with few continuous variables, for this project I used dictionaries/pickle files rather than Pandas. `compile_data.py` shows my process of compiling the three data sources into one dictionary, indexed by the Wikipedia movie ID. `nemo.txt` shows an example of what one entry looks like.
 

#### 3. Explore the Data 
As this was an exploratory analysis/visualization project, much of my work (answering the first three questions) falls into this step. `firstpass.ipynb` shows my first steps with the compiled .pkl file- simple frequences across variables, as well as beginning steps with Pygal.

I then wrote a series of helper functions (`helper_functions.py`) to avoid writing the same "get" queries from the dictionary. I added to this as the project went on. The `do_pygal.py` script contains some of the code for generating my charts, including a basic frequency of films from one genre over time. I used these two scripts to answer my first question about which genres make the most money in the box office.

For the second question, I ended up making a genre co-occurrence graph in Gephi, given that this was something I've done before but want to improve on. `genre_intersections.py` shows my process of generating the labels (genre names) and weights (genres that occur in the list for the same films).

For my analysis of the gender of film actors (`gender.py`), I wrote functions to answer both questions (about average age over time, and about the percent of actors that are male in each genre). 


#### 4. Model the Data 
Answering my last question-- about the relationship between revenue and the kinds of phrases in the plot summaries-- required some thinking. I wanted to measure correlation quantitatively, so I created a simple frequency-based model for the plot summary and revenue data (`summaries.py`). It's a little hacky, but works as follows:

- For every film, get the summary and the revenue
- Clean the summary (remove stopwords, punctuation, etc.)
- Generate n-grams (eg. unigrams, bigrams) from the summary
- Get a frequency of those n-grams for that summary
- Weight that frequency by the film's revenue 
- Add that term to a dictionary over all the films
- Normalize that dictionary over the max value (because we're dealing with very large numbers at this point)and take the log2 values (because the first normalizing step generates very small numbers). This generates more wieldy log values around -3.0, -10.0, etc. 
- Sort by the final normalized values, and look at the top phrases: these are the phrases "more likely" to appear in a plot summary for a higher-grossing film.

My findings are in the HTML page, but what I found was that using n > 2 (eg. trigrams) overfit the data; the top phrases ended up being taken straight from films I know to be very high-grossing, like *Titanic* and *Avatar*. 
Also, I removed stopwords so that "stock phrases" would not appear in the final counts, but in NLP terms, this wasn't totally ok for me to do (n-grams from a text with lots of words removed technically aren't real n-grams). But as an exploratory model, I think it's fine.
  
#### 5. Communicate and Visualize the Results 
I created a webpage that summarizes my findings from this project: 
[http://cs.wellesley.edu/~mokeefe2/cs249/movies](http://cs.wellesley.edu/~mokeefe2/cs249/movies)

### Challenges
The x-axes of my Pygal charts were very finicky. I couldn't figure out a way to get some years to show up and some to go away (for readability), so now you have to mouse over most of the charts to understand what's going on.

The hardest part of this project was figuring out how to answer my general questions in concrete ways-- I wish, for instance, that I'd done something more quantitative for the genre intersection question, rather than creating an explorer graph. Then again, I learned a lot more about how to work with layouts and statistics in Gephi, which I had been wanting to do after my preliminary work on the Ruhlman project. Further, the co-occurrence between genres on this project was a lot tighter than the abstract word co-occurrence in Ruhlman, and so it was somewhat easier to get the modularity groups closer together in the graph. 

### Reflecting and Moving Forward

It was great to hone several different skills on this project: data compilation, cleaning, parsing, statistical analysis, and visualization. I really liked using Pygal, and find that they're a great alternative to Plotly (you don't need API keys, and you can generate the graphs in fewer lines of code). Pygal does have relatively limited capabilities, but it suited my purposes and can cover the basic kinds of charts. I'm hoping to keep working with Pygal in the future, and I'm excited to continue to use my text analysis techniques I've picked up this semester.
