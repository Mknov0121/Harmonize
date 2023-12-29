from data_processing import load_data, spotify_data, path
import pandas 
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string

#---------------------------Download the requirements NLTK--------------------------------

#nltk.download('punkt')
#nltk.download('stopwords')

def clean_lyrics(lyrics):
    # Tokenización
    tokens = word_tokenize(lyrics)

    # To lower case 
    tokens = [word.lower() for word in tokens]

    # Delete signs 
    table = str.maketrans('', '', string.punctuation)
    stripped_tokens = [word.translate(table) for word in tokens]

    # Stop Words
    stop_words = set(stopwords.words('english'))  
    tokens_without_sw = [word for word in stripped_tokens if word not in stop_words]

    return tokens_without_sw

# Apply clean
spotify_data['cleaned_text'] = spotify_data['text'].apply(clean_lyrics)
spotify_data.to_csv('C:\\Users\\34640\\Desktop\\Saturdays.ai\\spotify_dset\\spotify_data_processed.csv', index=False)

#print(spotify_data['cleaned_text'].head())