import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=eec0063929fefb3e9e8e853d64bb0306&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500" + data['poster_path']





def recommendFunction(movie):
    movie_index = movies[movies['title'] ==  movie].index[0] #for fetching index of movie according to the movie title entered by user
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x: x[1])[1:6]
    
    recommend_movies = []
    rec_movies_poster = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommend_movies.append(movies.iloc[i[0]].title)
        rec_movies_poster.append(fetch_poster(movie_id))
    return recommend_movies, rec_movies_poster


movies_dictionary = pickle.load(open('movies_dictionary.pkl','rb'))
movies = pd.DataFrame(movies_dictionary)

similarity = pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommender System')

selected_movie = st.selectbox (
    "Select or enter the name of a movie",
    movies['title'].values
)


if st.button('Recommend Movie'):
    names,posters = recommendFunction(selected_movie)
    col1 , col2 , col3 , col4 , col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])
    