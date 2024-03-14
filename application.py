import streamlit as st

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


movies_dict=pickle.load(open('movie_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)

similarity=pickle.load(open('similarity.pkl','rb'))

st.title('Movie recommender system')
selected_movie_name=st.selectbox(
    'How would you like to be contacted?',
    movies['title'].values

    )


if st.button('Recommend movie'):
    names, posters = recommend(selected_movie_name)

    cols = st.columns(5)
    for i in range(5):
        with cols[i]:
            st.write(names[i])
            st.image(posters[i])


# if st.button('Recommend movie'):
#     names,posters=recommend(selected_movie_name)
#
#     col1,col2,col3,col4,col5=st.beta_columns(5)
#     with col1:
#         st.write(names[0])
#         st.image(posters[0])
#     with col2:
#         st.write(names[1])
#         st.image(posters[1])
#
#     with col3:
#         st.write(names[2])
#         st.image(posters[2])
#
#     with col4:
#         st.write(names[3])
#         st.image(posters[3])
#
#     with col5:
#         st.write(names[4])
#         st.image(posters[4])
    # recomandation=recommend(selected_movie_name)
    # for i in recomandation:
    #     st.write(i)


