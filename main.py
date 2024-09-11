import streamlit as st
import os
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(movie_id))
    data=response.json()
    return "https://image.tmdb.org/t/p/w500/" +data['poster_path']


def recommend(movie):
    movie_index=movies[movies['title']==movie].index[0]
    distances=similarity[movie_index]
    movies_list= sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]

    recommended_movie=[]
    recommended_movie_posters=[]
    for i in movies_list:

        movie_id=movies.iloc[i[0]].movie_id
        # fetch poster from api
        recommended_movie.append(movies.iloc[i[0]].title)
        recommended_movie_posters.append(fetch_poster(movie_id))
    return recommended_movie, recommended_movie_posters


movies_dict=pickle.load(open('C:/Users/asus/PycharmProjects/pythonProject/movie_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)

similarity=pickle.load(open('C:/Users/asus/PycharmProjects/pythonProject/similarity.pkl','rb'))

st.title('Movie recommender system')
selected_movie_name=st.selectbox(
    'recommend movie',
    movies['title'].values

    )


if st.button('Recommend movie'):
    names, posters = recommend(selected_movie_name)

    cols = st.columns(5)
    for i in range(5):
        with cols[i]:
            st.write(names[i])
            st.image(posters[i])