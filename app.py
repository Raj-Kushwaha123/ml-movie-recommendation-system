import streamlit as st
import pickle

# Load saved data
movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

st.set_page_config(page_title="Movie Recommender", layout="centered")

st.title("Movie Recommender System- ML Project")
st.write("A content-based recommendation system using cosine similarity (vectorization).")

def recommend(movie_name):
    index = movies[movies['title'] == movie_name].index[0]
    distances = similarity[index]

    movie_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended_movies = []
    for i in movie_list:
        recommended_movies.append(movies.iloc[i[0]].title)

    return recommended_movies

selected_movie = st.selectbox(
    "Select a movie:",
    movies['title'].values
)

if st.button("Recommend"):
    results = recommend(selected_movie)
    st.subheader("Recommended Movies")
    for movie in results:
        st.write("👉", movie)
