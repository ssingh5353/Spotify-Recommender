import pandas as pd
import numpy as np

def is_favorite_song(num_listens):
    if(num_listens >= 15):
        return "Favorite"
    return "Not favorite"


def combine_genres(df):
    unique_songs = list(df.trackName.unique())
    genres = list(df.genre.unique())
    cols = list(df.columns)
    
    song_genre_pair = {}
    for song in unique_songs:
        song_genre_pair[song] = []
    

    for row in df.itertuples():
        songName = row.trackName
        songGenre = row.genre
        song_genre_pair[songName].append(songGenre)
        
    new_df = df.drop(['genre','popularity'],axis = 1).drop_duplicates()

    for genre in genres:
        new_df[genre] = np.nan

    new_df.reset_index(inplace=True)

    for i in range(len(new_df)):
        songName = new_df.iloc[i]['trackName']
        for genre in genres:
            if(genre in song_genre_pair[songName]):
                new_df.at[i, genre] = 1
            else:
                new_df.at[i, genre] = 0

    new_df.drop(['index'],axis = 1, inplace = True)

    return new_df