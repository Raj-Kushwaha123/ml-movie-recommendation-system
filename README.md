<img width="1430" height="881" alt="image" src="https://github.com/user-attachments/assets/3ec39641-c97b-47a4-825f-fa2dd6eb651f" />

# Movie Recommender System

This project implements a content-based movie recommender system using machine learning techniques.
The system recommends movies similar to a selected movie based on textual metadata.

# Project Overview

Recommendation Type: Content-Based Filtering

Techniques Used: TF-IDF Vectorization, Cosine Similarity

Dataset: TMDB 5000 Movie Metadata (CSV format)

Deployment: Streamlit (Local)

# How the Recommendation System Works

Movie metadata such as genres, overview, cast, crew, and keywords are combined.
Text data is transformed into numerical vectors using TF-IDF.
Cosine similarity is computed between movie vectors to measure similarity.
Movies with the highest similarity scores are recommended.

# Required Dataset Files

tmdb_5000_movies.csv
tmdb_5000_credits.csv
Dataset Source :- 
  https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata
