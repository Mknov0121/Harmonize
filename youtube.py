from Recomendation import recommend_song_interface
import gradio as gr
import requests



def search_youtube(song, artist, api_key):
    query = f"{song} by {artist}"
    search_url = "https://www.googleapis.com/youtube/v3/search"
    params = {
        'part': 'snippet',
        'q': query,
        'type': 'video',
        'maxResults': 1,
        'key': api_key
    }

    response = requests.get(search_url, params=params)
    response_json = response.json()
    #print("Response from YouTube API:", response_json)

    if 'items' in response_json and response_json['items']:
        video_id = response_json['items'][0]['id']['videoId']
        youtube_link = f"https://www.youtube.com/watch?v={video_id}"
        return youtube_link
    else:
        return "No se encontraron resultados."

def add_youtube_links(recommendations, api_key):
    recommendations_with_links = []
    for recommendation in recommendations:
        if " by " in recommendation:  # Si la recomendación no es una cadena vacía
            song, artist = recommendation.split(" by ", 1)
            youtube_link = search_youtube(song, artist, api_key)
            recommendations_with_links.append(youtube_link)
        else:
            recommendations_with_links.append(recommendation)

    return recommendations_with_links

def recommend_with_youtube_links(song_name, artist_name):
    api_key = "AIzaSyAp-D7Mfafd6gJQo2gtAXRXwDlG8_uNXnU"
    recommendations = recommend_song_interface(song_name, artist_name)
    recommendations_with_links = add_youtube_links(recommendations, api_key)

    return recommendations_with_links

# Configuración de la interfaz Gradio
"""iface = gr.Interface(
    fn=recommend_with_youtube_links,
    inputs=[
        gr.Textbox(placeholder="Ingrese el título de la canción", label="Título de la Canción"),
        gr.Textbox(placeholder="Ingrese el nombre del artista", label="Nombre del Artista")
    ],
    outputs=[
    gr.Text(label="Recomendación 1"),
    gr.Text(label="Recomendación 2"),
    gr.Text(label="Recomendación 3"),
    gr.Text(label="Recomendación 4"),
],
    title="Recomendador de Canciones con Enlaces de YouTube",
    description="Ingrese el título de una canción y el nombre del artista.",
)

iface.launch()"""
