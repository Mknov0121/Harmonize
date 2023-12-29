# responses.py
from Recomendation import recommend_song_interface
from youtube import add_youtube_links

# Asegúrate de configurar tu clave de API de YouTube aquí
API_KEY = "AIzaSyAp-D7Mfafd6gJQo2gtAXRXwDlG8_uNXnU"

def get_recommendation(titulo, artista):
    recommendations = recommend_song_interface(titulo, artista)
    recommendations_with_links = add_youtube_links(recommendations, API_KEY)
    
    """formatted_recommendations = []

    for recommendation in recommendations_with_links:
        # Asegúrate de que cada recomendación sea una cadena
        if isinstance(recommendation, tuple) or isinstance(recommendation, list):
            # Si es una tupla o lista, conviértela en una cadena
            recommendation_str = " - ".join(recommendation)
            formatted_recommendations.append(recommendation_str)
        else:
            formatted_recommendations.append(recommendation)"""

    return recommendations_with_links