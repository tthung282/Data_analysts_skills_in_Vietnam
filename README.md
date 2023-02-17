# Data_analysts_skills_in_Vietnam
 A project for personal use, inspiration from Luke Barousse
 
SOME MAIN POINTS:

###Getting the data### (Serpapi.com)
Google job is the target for this project since it collect data from all other job sites (Linkedin, topcv, vietnamwork... you name it)
However, the information is displayed in a summarized manner so it's difficult to create a spider and scraping all those links.
In the meantime, serpapi provide us an api code to collect those data easily. So this is the final choice.

###Cleaning the data### (NLTK library)
NLTK library help spliting long strings into seperated words and put them in the library. We're gonna use this to sort out all the keywords about skills, tools, ... from the discription that the data provide

###Analyzing + designing with pandas + streamlit###
Simple line-chart and bar-chart
The hard parts in streamlit was creating filters
