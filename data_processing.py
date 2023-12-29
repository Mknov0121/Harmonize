import pandas as pd
import numpy as np
import sys
import codecs
#-------------------Load_data, function that loads the Spotify Dataset 1921-2020, 600k+-------------------------- 
#-------------------Tracks and checks with an error check if the data has been loaded correctly.----------------

def load_data (path):
    try:
        df = pd.read_csv(path)
        return df
    except FileNotFoundError:
        print(f"The document is not found in the directory: {path}")
        return None
    except Exception as e:
        print(f"An error occurred loading the file: {e}")
        return None
path = 'path'
spotify_data = load_data(path)

spotify_data.columns = ['artist', 'song', 'link', 'text']



if spotify_data is not None:
    print("-----------Suscessfully loaded-------------")
    

   # print(spotify_data.isnull().sum())
#-----------Fill up white space-----------#
    for col in spotify_data.columns:
        spotify_data[col] = spotify_data[col].fillna(spotify_data[col].mode()[0])

#-----------Convert to lower case and delete special characters-----------#
        spotify_data[col] = spotify_data[col].str.lower().str.replace('[^\w\s]', '', regex=True)


#-----------Delete duplicates-----------#
    spotify_data = spotify_data.drop_duplicates()

    #print(spotify_data.isnull().sum())
else:
    print("No spotify data")


    
