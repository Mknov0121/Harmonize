Welcome to the project where music meets cutting-edge technology. This project brings together data science, natural language processing and application development to offer a unique song recommendation experience integrated with popular platforms like Discord and YouTube.

This project uses a Spotify dataset to recommend songs based on user preferences. Through vectorization and vector representation, song lyrics are transformed into analyzable data, allowing the system to suggest similar songs. In addition, it integrates with the YouTube API to provide direct links to recommended songs and a Discord bot to interact with users.

Features Song Recommendation: Based on NLP and Word2Vec techniques to analyze and suggest songs. YouTube integration: Direct links to YouTube videos for each recommended song. Discord Bot: Interactive interface to receive song recommendations within Discord. Data-Driven: Uses an extensive Spotify dataset for analysis and recommendations. Project Structure The project is divided into several scripts and modules, each with a specific purpose:

Data Processing: Spotify data cleaning and preparation. Vectorization: Vectorization of song lyrics for analysis. Recommendation: Song recommendation system based on similarities. YouTube Integration: Module to integrate recommendations with YouTube links. Discord Bot: An interactive bot for Discord that uses the recommendation system. Requirements Python 3.x Libraries: discord.py, numpy, pandas, gensim, requests, gradio YouTube API Key Discord Bot Token Installation and Configuration Clone the repository: git clone [repository URL]. Install dependencies: pip install -r requirements.txt Configure the YouTube API keys and Discord token in the corresponding files. Execute the scripts as needed.

Using To use the Discord bot:

Make sure the bot is active and connected to your Discord server. Use the /recommend <title> command to get recommendations. Explore the YouTube recommendations and links provided by the bot. 
