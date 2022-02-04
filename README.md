# map-reduce-bairy
# Python Map Reduce

Basic piping introduction and concepts needed in preparation for working with big data solutions.

## Big Data Processing Skills

1. Understand how to pipe source data into mapper.
2. Understsand how to pipe mapper output into (temporary) sort.
3. Understand how to pipe sorted mapper output key-value pairs into reducer.
4. Understand how to redirect output to file (sink) containing valuable information. 

## Outcomes

1. Understand value of map() and reduce() in big data. 
2. Chain together processes (e.g. multiple MR jobs)
3. Use big data processing to get the main idea from a large text corpus.
4. Understand functional programming approaches and reasons. 
5. Understand challenges of writing code that can be distributed and processed concurrently. 

## Requirements

- Install the Miniconda 3 version for Python + common packages
- Install Visual Studio Code for text editing

## Recommended 

- Add Open PowerShell Here as Administrator to File Explorer context menu.
- Add Open Command Window Here as Administrator to File Explorer context menu.
- Add Open Anaconda Prompt Here as Administrator to File Explorer context menu.

OR be able to cd (change directory) to get to folder. 


## Interesting Custom Big Data Story

I found the Kaggle Tweets dataset regarding restaurants serving pizza per capita (100,000 residents) across the U.S.?
I wondered "cities have the most restaurants serving pizza per capita (100,000 residents)?"

From the initial dataset, I'll map to key-value pairs: cities, count. 
Then, I'll use the terminal "sort" to get them sorted in case they aren't. 
Then, I'll reduce all the key-value pairs for one city to a single value: city, countOfRestaurants. 

```PowerShell
cat CustomDataSet.csv | python CustomDataMapper.py | sort  | python CustomDataReducer.py > bairy-out.txt

```



![Cities with more number of pizza restaurants per capita](TopTenCities.PNG)

The result is only 240 records, so I'll use Excel to chart it. 
Excel Data / Filter.  Then, sort by count reversed - or better yet, just take the "Top 10". 
Excel Insert / Recommended Chart - seems to look nice. Found out the top 10 cities with more number of restaurants per capita(100,000 residents)

From the above chart we can see the top 10 cities with more number of pizza restaurants per capita(100,000)



## Repository

- [https://github.com/VarshithReddyBairy/map-reduce-bairy](https://github.com/VarshithReddyBairy/map-reduce-bairy)
