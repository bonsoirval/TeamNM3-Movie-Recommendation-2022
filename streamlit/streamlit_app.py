import pickle
import streamlit as st
import pandas as pd
import requests as req


header = st.container()
content_select = st.container()
content_display = st.container()
collaborative_select = st.container()
collaborative_display = st.container()
visuals = st.container()
dataset = st.container()

# api_key="8265bd1679663a7ea12ac168da84d2e8"
# language="en-US"
# movie_base_path = "https://api.themoviedb.org/3/movie/{movie_id}?"
# image_path = "https://image.tmdb.org/t/p/w500/"
# # functions declaration
# def fetch_poster(movie_id):
#     url = movie_base_path+api_key+language # build the complete url
#     data = req.get(url)
#     data = data.json()
#     poster_path = data["poster_path"]  # movie poster path
#     full_path = image_path+poster_path
#     return full_path

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = req.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path


def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x:x[1])
    recommended_movies_names = []
    recommended_movies_posters = []
    for index in distances[1:6]:
        # fetch the movie poster
        movie_id = movies.iloc[index[0]].movie_id
        recommended_movies_posters.append(fetch_poster(movie_id))
        recommended_movies_names.append(movies.iloc[index[0]].title)
    return recommended_movies_names, recommended_movies_posters

movies = pickle.load(open('model/movie_list.pkl', 'rb'))
similarity = pickle.load(open("model/similarity.pkl", 'rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or Select a movie from the dropdown",
    movie_list
)

with header:
    st.title("Movie Recommendation System EDSA-TeamNM3")
with st.sidebar:
    genre_options = ['Kids', "Horror"]

    options = ['Kids', "Horror"]
    min_year = 1990
    max_year = 2022
    year_value = 1990
    year_step = 2
    min_img_pp = 4
    max_img_pp = 8
    img_value = 4
    img_step = 2
    model_options = ["Content Base Recommendation", "Collaborative Base Recommendation"]

    genre = st.selectbox("Select Choice Genre: ", options=genre_options)
    date_range = st.slider("Movie Between: ", min_value=min_year, max_value=max_year, value=year_value, step=year_step)
    image_per_page = st.slider("Images per page: ", min_value=min_img_pp, max_value=max_img_pp, value=img_value,step=img_step)
    model_base = st.selectbox("Recommend Using: ", options=model_options)
    st.button("Recommend")

# with content_select:
#     st.subheader("Content Based Recommendation")
#     # content_mv_type = content_select.selectbox("Select Recommendation Criteria:",options=['Genre', 'Year'], index=0)
#     st.markdown(f""" Chosen Genre: {genre}""")

with collaborative_select:
    pass
    # st.subheader("Collaborative Based Recommendation")
    # content_mv_type = collaborative_select.selectbox("Select Recommendation Criteria:",options=['Producer', 'Year Produced'], index=0)


if st.button('Show Recommendation'):
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])

    # genre = st.selectbox("Select Choice Genre: ", options=options)
    # date_range = st.slider("Movie Between: ", min_value=min_year, max_value=max_year, value=year_value, step=year_step)
    # image_per_page = st.slider("Images per page: ", min_value=min_img_pp, max_value=max_img_pp, value=img_value,step=img_step)


# with content_select:
#     st.subheader("Content Based Recommendation")
#     # content_mv_type = content_select.selectbox("Select Recommendation Criteria:",options=['Genre', 'Year'], index=0)


# with collaborative_select:
#     st.subheader("Collaborative Based Recommendation")
#     # content_mv_type = collaborative_select.selectbox("Select Recommendation Criteria:",options=['Producer', 'Year Produced'], index=0)
