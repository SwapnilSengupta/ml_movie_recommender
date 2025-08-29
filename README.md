# 🎬 Movie Recommendation System

## 📌 Project Overview
This project is a **Content-Based Movie Recommendation System** built using **Natural Language Processing (NLP)** and **Machine Learning** techniques.  
It suggests movies similar to a user-selected movie by analyzing different features of movies such as **overview, genres, keywords, cast, and crew (director)**.  

The system uses a **Bag of Words model with cosine similarity** to measure closeness between movies and recommend the top matches.

---

## ⚙️ How It Works
1. **Dataset**  
   - The dataset contains around **5000 movies** with information like title, overview, genres, cast, crew, and keywords.
   - Columns used for building recommendations:
     - `overview` → storyline/description
     - `genres` → movie genres
     - `keywords` → descriptive tags
     - `cast` → main actors/actresses
     - `crew` → director
     
2. **Data Preprocessing**  
   - Parsing JSON-like columns (`genres`, `keywords`, `cast`, `crew`) into structured lists.
   - Cleaning the `overview` column by removing punctuation, extra spaces, and unnecessary characters using **regular expressions**.
   - Handling missing values and empty lists (`[]`) by applying logical defaults.
   - Combining all important features into a new column called **`tags`**.

3. **Feature Engineering**  
   - Text normalization (lowercasing, removing stopwords, tokenization).
   - Applying **Bag of Words (CountVectorizer)** to convert text into vectors.
   - Creating a **similarity matrix** using **cosine similarity**.

4. **Recommendation**  
   - For a given movie, the system finds **n most similar movies** based on vector similarity (angular distance).
   - Recommendations are displayed instantly via the **Streamlit web app**.

---

## 🖥️ Tech Stack
- **Python** 🐍  
- **Libraries**: Pandas, NumPy, Scikit-learn, NLTK, Ast, Regular Expressions  
- **Frontend**: Streamlit  
- **Deployment**: Heroku / Render  

---

## 🚀 Features
✅ Clean and intuitive **Streamlit web interface**  
✅ Suggests **Top 5 similar movies** instantly  
✅ Handles missing or empty values logically  
✅ Optimized text processing for accurate recommendations  
✅ Deployed and accessible online  

---

## 📷 Demo
👉 Upload a screenshot or GIF of your app running here.  

---

## 📂 Project Structure

