# import streamlit as st
# import pickle
# import pandas as pd
# import requests
#
# def fetch_poster(movie_id):
#     response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(movie_id))
#     data = response.json()
#     return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
#
# def fetch_movie_link(movie_id):
#     return "https://legal-streaming-service.com/watch?movie_id=" + str(movie_id)
#     # Implement this function to return the URL of the movie
#     # For now, it returns a placeholder text
#     #return "Link not available"
#
# def recommend(movie):
#     movie_index = movies[movies['title'] == movie].index[0]
#     distances = similarity[movie_index]
#     movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
#
#     recommended_movies = []
#     recommended_movie_posters = []
#     recommended_movie_links = []
#     for i in movies_list:
#         movie_id = movies.iloc[i[0]].movie_id
#         recommended_movies.append(movies.iloc[i[0]].title)
#         recommended_movie_posters.append(fetch_poster(movie_id))
#         recommended_movie_links.append(fetch_movie_link(movie_id))
#     return recommended_movies, recommended_movie_posters, recommended_movie_links
#
# movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
# movies = pd.DataFrame(movies_dict)
#
# similarity = pickle.load(open('similarity.pkl', 'rb'))
#
# st.title('Movie recommender system')
# selected_movie_name = st.selectbox('Select a movie:', movies['title'].values)
#
# if st.button('Recommend movie'):
#     names, posters, links = recommend(selected_movie_name)
#     cols = st.columns(5)
#     for i in range(5):
#         with cols[i]:
#             st.write(names[i])
#             st.image(posters[i])
#             st.markdown(f"Watch here" if links[i] != "Link not available" else "Link to watch is not available.")
#
#
#


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
