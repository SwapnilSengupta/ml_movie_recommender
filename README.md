# 🎬 Movie Recommendation System

# Live App Link : https://ml-movie-recommender-1hwg.onrender.com/

## 📌 Project Overview
This project is a **Content-Based Movie Recommendation System** built using **Natural Language Processing (NLP)** and **Machine Learning** techniques.  
It suggests movies similar to a user-selected movie by analyzing different features of movies such as **overview, genres, keywords, cast, and crew (director)**.  

The system uses a **Bag of Words model with cosine similarity** to measure closeness between movies and recommend the top matches.

---

## ⚙️ How It Works
1. **Dataset**
   Source : Kaggle TMDb 5000
   - The dataset contains around **5000 movies** with information like title, overview, genres, cast, crew, and keywords,votes,languages,etc.
   - Columns used for building recommendations:
     - `overview` → storyline/description
     - `genres` → movie genres
     - `keywords` → descriptive tags
     - `cast` → main actors/actresses
     - `crew` → director
    
2. **Data Loading and Inspection**
     
3. **Data Preprocessing**  
   - Parsing JSON-like columns (`genres`, `keywords`, `cast`, `crew`) into structured lists.
   - Cleaning the `overview` column by removing punctuation, extra spaces, and unnecessary characters using **regular expressions**.
   - Handling missing values and empty lists (`[]`) by applying logical defaults.
   - Combining all important features into a new column called **`tags`**.

4. **Feature Engineering**  
   - Text normalization (lowercasing, removing stopwords, tokenization).
   - Applying **Bag of Words (CountVectorizer)** to convert text into vectors.
   - Creating a **similarity matrix** using **cosine similarity**.

5. **Recommendation**  
   - For a given movie, the system finds **5 most similar movies** based on vector similarity (angular distance).
   - Recommendations are displayed instantly via the **Streamlit web app**.

6. 🎬 Frontend (Streamlit App)

   The frontend of this project is built using **Streamlit**, providing an interactive and user-friendly web interface.

   - Users can search for any movie by typing its name into the input box.  
   - Once a movie is selected, the system fetches **top 5 similar recommendations** using the pre-computed similarity matrix.  
   - For each recommended movie, the **poster is retrieved dynamically** from [TMDb API](https://www.themoviedb.org/documentation/api), using the corresponding movie ID from the dataset.  
   - Results are displayed in a clean layout with movie titles and posters side by side for a smooth user experience.  

   This ensures the model’s results are not just textual but also visually engaging.


---

## 🖥️ Tech Stack
- **Python** 🐍  
- **Libraries**: Pandas, NumPy, Scikit-learn, NLTK, Ast, Regular Expressions  
- **Web App**: Streamlit,HTML,CSS,JS  
- **Deployment**: Render  

---

## 🚀 Features
✅ Clean and intuitive **Streamlit web interface**  
✅ Suggests **Top 5 similar movies** instantly  
✅ Handles missing or empty values logically  
✅ Optimized text processing for accurate recommendations  
✅ Deployed and accessible online  

---

