from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import numpy as np
from vectorization import spotify_data
import json
import gradio as gr
from gradio.components import Textbox
from ast import literal_eval
spotify_data_processed = pd.read_csv('C:\\Users\\34640\\Desktop\\Saturdays.ai\\spotify_dset\\dataset_modificado.csv')

def convert_string_to_array(str_vector):
    # Si str_vector ya es un array de NumPy, devolverlo directamente
    if isinstance(str_vector, np.ndarray):
        return str_vector

    try:
        cleaned_str = str_vector.replace('[', '').replace(']', '').replace('\n', ' ').replace('\r', '').strip()
        vector_elements = [float(item) for item in cleaned_str.split()]
        return np.array(vector_elements)
    except ValueError as e:
        print("Error:", e)
        return np.zeros((100,))


spotify_data_processed['song_vector'] = spotify_data_processed['song_vector'].apply(convert_string_to_array)


# Aplicar la función a las primeras filas para ver los resultados
"""sample_data = spotify_data_processed['song_vector'].head()
converted_vectors = sample_data.apply(convert_string_to_array)
print(converted_vectors)"""



def recommend_song(song_name, artist_name, spotify_data_processed, top_n=4):
    # Filtrar para encontrar la canción específica
    specific_song = spotify_data_processed[(spotify_data_processed['song'] == song_name)
                                            & (spotify_data_processed['artist'] == artist_name)]

    # Verificar si la canción existe en el dataset
    if specific_song.empty:
        return pd.DataFrame({"Error": ["Canción no encontrada en la base de datos."]})


    # Obtener el vector de la canción específica
    song_vec = specific_song['song_vector'].iloc[0]

    # Asegurarte de que song_vec sea un array de NumPy
    if isinstance(song_vec, str):
        song_vec = convert_string_to_array(song_vec)

    all_song_vectors = np.array(spotify_data_processed['song_vector'].tolist())

    # Calcular similitudes
    similarities = cosine_similarity([song_vec], all_song_vectors)[0]

    # Obtener los índices de las canciones más similares
    top_indices = np.argsort(similarities)[::-1][1:top_n+1]

    # Devolver los nombres y artistas de las canciones más similares
    recommended_songs = spotify_data_processed.iloc[top_indices][['song', 'artist']]
    return recommended_songs




def recommend_song_interface(song_name, artist_name):
    recommendations_df = recommend_song(song_name, artist_name, spotify_data_processed)
    
    # Verificar si el DataFrame está vacío o si las columnas necesarias están presentes
    if isinstance(recommendations_df, pd.DataFrame) and not recommendations_df.empty and {'song', 'artist'}.issubset(recommendations_df.columns):
        recommendations_list = recommendations_df[['song', 'artist']].values.tolist()
        formatted_recommendations = ["{} by {}".format(song, artist) for song, artist in recommendations_list]
        # Rellenar con cadenas vacías si hay menos de 4 recomendaciones
        while len(formatted_recommendations) < 4:
            formatted_recommendations.append("")
        return formatted_recommendations[:4]
    else:

       
        random_song = spotify_data_processed.sample() # Escoge una linea la azar de todo el conjunto de datos .sample()
        random_song_name = random_song['song'].iloc[0] # Extrae el valor de la columna song de la fila sample (Nombre)
        random_artist_name = random_song['artist'].iloc[0] # Extrae el valor de la columna artist de la fila sample (Nombre)
        
        # Obtener recomendaciones para la canción aleatoria
        random_recommendations_df = recommend_song(random_song_name, random_artist_name, spotify_data_processed)
        random_recommendations_list = random_recommendations_df[['song', 'artist']].values.tolist()
        formatted_random_recommendations = ["{} by {}".format(song, artist) for song, artist in random_recommendations_list]
        
        # Rellenar con cadenas vacías si hay menos de 4 recomendaciones
        while len(formatted_random_recommendations) < 4:
            formatted_random_recommendations.append("")
        return formatted_random_recommendations[:4]

# Ejemplo de uso
# Asegúrate de que spotify_data_processed es un DataFrame de Pandas válido con las columnas 'song' y 'artist'
recommendations = recommend_song_interface("song_name", "artist_name")


