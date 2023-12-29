from gensim.models import Word2Vec
import pandas as pd


spotify_data= pd.read_csv('C:\\Users\\34640\\Desktop\\Saturdays.ai\\spotify_dset\\spotify_data_processed.csv')




# Asumiendo que spotify_data['cleaned_text'] contiene listas de palabras (tokens)
spotify_data['cleaned_text'] = spotify_data['cleaned_text'].apply(eval)

model = Word2Vec(sentences=spotify_data['cleaned_text'], vector_size=100, window=10, min_count=1, workers=5)
# Guardar el modelo
model.save("word2vec_model.model")
