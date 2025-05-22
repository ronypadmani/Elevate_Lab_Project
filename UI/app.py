import streamlit as st
import pickle
import pandas as pd


movies_df = pickle.load(open('movies.pkl', 'rb'))
movies_list = movies_df['title'].values

similarity = pickle.load(open('similarity.pkl', 'rb'))


def recommend(movie):
    movie_index = movies_df[movies_df['title'] == movie].index[0]
    distances = similarity[movie_index]

    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movie_list:
        movie_id = i[0]
        # fetch poster from API
        recommended_movies.append(movies_df.iloc[i[0]].title)
    return recommended_movies


st.title('Movie Recommender System')

selected_movies_name = st.selectbox(
    'Select a movie you like:',
    movies_list)

if st.button('Recommend'):
    recommendations = recommend(selected_movies_name)
    for i in recommendations:
        st.write(i)
