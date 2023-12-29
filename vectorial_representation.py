import numpy as np
from vectorization import model, spotify_data

# Función para convertir una canción en un vector promedio de sus palabras
def song_vector(tokens, model):
    # Filtrar palabras que están en el modelo
    tokens = [word for word in tokens if word in model.wv.key_to_index]

    if len(tokens) == 0:
        return np.zeros(model.vector_size)

    # Calcular el promedio de los vectores de las palabras
    song_vec = np.mean([model.wv[word] for word in tokens], axis=0)
    return song_vec

# Aplicar esta función a cada canción en tu dataset
spotify_data['song_vector'] = spotify_data['cleaned_text'].apply(lambda x: song_vector(x, model))
spotify_data.to_csv('Path', index=False)


