import streamlit as st
import streamlit.components.v1 as components
from sklearn.metrics.pairwise import linear_kernel
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import time
import matplotlib.pyplot as plt

df1 = pd.read_csv('./tmdb_5000_credits.csv')
df2 = pd.read_csv('./tmdb_5000_movies.csv')

df1.columns = ['id', 'tittle', 'cast', 'crew']
df2 = df2.merge(df1, on='id')

tfidf = TfidfVectorizer(stop_words='english')
df2['overview'] = df2['overview'].fillna('')
tfidf_matrix = tfidf.fit_transform(df2['overview'])

cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
indices = pd.Series(df2.index, index=df2['title']).drop_duplicates()


def get_recommendations(title, cosine_sim=cosine_sim):
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]
    movie_indices = [i[0] for i in sim_scores]
    return df2['title'].iloc[movie_indices]


st.set_option('deprecation.showPyplotGlobalUse', False)

components.html(
    """
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Anton&family=Roboto+Condensed&display=swap" rel="stylesheet">
    <div style= "color: #E34234; font-weight: bold; text-align: left; font-size: 50px; font-family: 'Roboto Condensed', sans-serif;" >
    Pocket Flick
    <div style= "color: grey; text-align: left; font-size: 10px; font-family: Trebuchet MS;" >
    v.1.0.0
    <br></br>
    </div>
    </div>
    """,
    height=100,
)


with st.spinner(text="Loading model..."):
    time.sleep(5)

st.subheader("Recommended Movies For You")

user_input = st.text_input("")

if user_input:
    try:
        with st.spinner(text="Finding recommendations..."):
            time.sleep(3)

        st. write("Here are our top recommendations.")
        st.write(get_recommendations(user_input))
    except KeyError:
        st.error("Please try a different title.")

st.sidebar.header("Top Movies of All Time")
st.sidebar.image(
    "https://m.media-amazon.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_.jpg")
st.sidebar.image(
    "https://m.media-amazon.com/images/M/MV5BM2M1MmVhNDgtNmI0YS00ZDNmLTkyNjctNTJiYTQ2N2NmYzc2XkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_.jpg")
st.sidebar.image(
    "https://m.media-amazon.com/images/M/MV5BMTY4NzcwODg3Nl5BMl5BanBnXkFtZTcwNTEwOTMyMw@@._V1_.jpg")
st.sidebar.image(
    "https://m.media-amazon.com/images/M/MV5BMDFkYTc0MGEtZmNhMC00ZDIzLWFmNTEtODM1ZmRlYWMwMWFmXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_FMjpg_UX1000_.jpg")
