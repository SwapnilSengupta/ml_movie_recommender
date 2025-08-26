import pandas as pd
import streamlit as st
import pickle
movie_info = pickle.load(open(r'C:\Users\Swapnil Sengupta\ML Projects\Movie Recommender System\movie_dict.pkl', 'rb'))
df = pd.DataFrame(movie_info)

st.title('Movie Recommender System')

option = st.selectbox(
    "How would you like to be contacted?",
    df['title'].values,
)

st.write("You selected:", option)
if st.button("Recommend"):
    st.write("Ciao")
