import pickle
import streamlit as st
import pandas as pd


header = st.container()
content_select = st.container()
content_display = st.container()
collaborative_select = st.container()
collaborative_display = st.container()
visuals = st.container()
dataset = st.container()

with header:
    st.title("Movie Recommendation System EDSA-TeamNM3")
with st.sidebar:
    options = ['Kids', "Horror"]
    min_year = 1990
    max_year = 2022
    year_value = 1990
    year_step = 2
    min_img_pp = 4
    max_img_pp = 8
    img_value = 4
    img_step = 2

    genre = st.selectbox("Select Choice Genre: ", options=options)
    date_range = st.slider("Movie Between: ", min_value=min_year, max_value=max_year, value=year_value, step=year_step)
    image_per_page = st.slider("Images per page: ", min_value=min_img_pp, max_value=max_img_pp, value=img_value,step=img_step)


with content_select:
    st.subheader("Content Based Recommendation")
    content_mv_type = content_select.selectbox("Select Recommendation Criteria:",options=['Genre', 'Year'], index=0)


with collaborative_select:
    st.subheader("Collaborative Based Recommendation")
    content_mv_type = collaborative_select.selectbox("Select Recommendation Criteria:",options=['Producer', 'Year Produced'], index=0)
