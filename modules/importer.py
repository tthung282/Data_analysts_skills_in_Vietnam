import pandas as pd
import streamlit as st

class DataImport:
    """"
    Import data from CSV file
    """
    def __init__(self):
        pass

    @st.cache_data(ttl=60*60) # ttl of one hour to keep memory in cache
    def fetch_and_clean_data():
        data_url = 'modules/test2.csv'
        jobs_data = pd.read_csv(data_url).replace("'","", regex=True)
        jobs_data.date_time = pd.to_datetime(jobs_data.date_time)
        jobs_data= jobs_data.drop(labels=['Unnamed: 0','Unnamed: 0.1','Unnamed: 0.2','Unnamed: 0.3','Unnamed: 0.4','Unnamed: 0.5', 'index'], axis=1, errors='ignore')
        jobs_data.description_tokens = jobs_data.description_tokens.str.strip("[]").str.split(",") # fix major formatting issues with tokens
        jobs_data.description_tokens = jobs_data.description_tokens.apply(lambda row: [x.strip(" ") for x in row]) # remove whitespace from tokens
        return jobs_data