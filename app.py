import pandas as pd
import streamlit as st
import requests
import pickle
import streamlit.components.v1 as components
st.set_page_config(page_title="Movie Recommender", page_icon="🎬", layout="wide")
st.markdown(
    """
    <style>
      
    /* app background */
    .stApp {
        background: linear-gradient(to right, #0f2027, #203a43, #2c5364);
        color: white;
    }

    /* Button styling: visible background + readable text */
    .stButton>button {
        background-color: #FFD700 !important; /* gold */
        color: #0b0b0b !important;            /* dark text for contrast */
        border: none;
        padding: 10px 22px;
        border-radius: 10px;
        font-weight: 700;
        box-shadow: 0 6px 18px rgba(0,0,0,0.25);
        transition: transform 0.18s ease, box-shadow 0.18s ease, opacity 0.18s ease;
    }
    .stButton>button:hover {
        background-color: #3FA224 !important;  /* orange-red */
        color: white !important;               /* text becomes white */
        transform: translateY(-3px) scale(1.08) rotate(-1deg);

        box-shadow: 0 10px 28px rgba(0,0,0,0.35);
        opacity: 1;
        letter-spacing: 1px;
        transition: all 0.25s ease-in-out;
    }

    /* Reduce gap under the small header text (select label) */
    .small-gap {
        margin-top: 10px !important;
        margin-bottom: -10000px !important;
        padding:10px;
        display: block;
    }

    /* Recommendation card styling */
    .reco-card {
        padding: 12px;
        border-radius: 14px;
        background-color: rgba(30,30,30,0.95);
        text-align: center;
        box-shadow: 2px 6px 18px rgba(0,0,0,0.45);
    }
    .reco-card h4 {
        color: #FFD700;
        margin: 8px 0 10px 0;
        font-size: 16px;
        min-height: 44px; /* keeps title heights consistent */
        overflow: hidden;
    }

    /* Make posters bigger and consistent, crop nicely */
    .reco-card img {
        border-radius: 10px;
        width: 100%;
        height: 360px;         /* increased size */
        object-fit: cover;     /* crop without distortion */
        transition: transform 0.22s ease;
    }
    .reco-card img:hover {
        transform: scale(1.03); /* subtle zoom on hover */
    }

    /* Title: keep on a single line (no wrapping) but responsive */
    .title-nowrap {
        text-align: center;
        color: #FFD700;
        white-space: nowrap;     /* prevent emoji wrapping */
        font-size: 34px;        /* slightly smaller so it fits better */
        margin-bottom: 6px;
        font-weight:700;
    }

    /* footer small styling */
    .footer {
        text-align:center;
        margin-top: 18px;
        color:#e8e8e8;
        opacity:0.9;
    }
 




    </style>

    """,
    unsafe_allow_html=True
)

movie_info = pickle.load(open(r'movie_dict.pkl', 'rb'))
df = pd.DataFrame(movie_info)
similarity = pickle.load(open(r'similarity.pkl', 'rb'))
API_KEY = "3a9a481f894a34e343750ce28b7f9dbc"
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}"
    response = requests.get(url)
    data = response.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500" + poster_path
    return full_path


def recommend(movie):
    movie_index = df[df['title'] == movie].index[0]
    similarity_arr = sorted(list(enumerate(similarity[movie_index].copy())), reverse=True, key=lambda x: x[1])
    count = 0
    rec_list=[]
    pos_list=[]
    for i in similarity_arr:
        mov_ind = i[0]
        mov_id= df.iloc[mov_ind]['id']
        if (mov_ind != movie_index):

            # print(mov_ind)
            rec_list.append((df.iloc[mov_ind].title))
            pos_list.append(fetch_poster(mov_id))
            count += 1
            if (count == 5):
                break
    return rec_list,pos_list

# st.title('Movie Recommender System')
#
# option = st.selectbox(
#     "Select a movie that you liked watching/would like to watch",
#     df['title'].values,
# )



# Title (nowrap so emoji stays on same line)
st.markdown("<div class='title-nowrap'>🎬 Movie Recommender System 🎬</div>", unsafe_allow_html=True)

# Smaller gap header for selectbox
st.markdown("<div class='small-gap'><strong>🔍 Select a movie that you liked watching / would like to watch</strong></div>", unsafe_allow_html=True)
option = st.selectbox("", df['title'].values)

# if st.button("Recommend"):
#     recommendations,poster_list=recommend(option)
#     # for i in recommendations:
#     #     st.write(i)
#
#
#
#     col1, col2, col3,col4,col5 = st.columns(5)
#
#     with col1:
#         st.text(recommendations[0])
#         st.image(poster_list[0])
#     with col2:
#         st.text(recommendations[1])
#         st.image(poster_list[1])
#     with col3:
#         st.text(recommendations[2])
#         st.image(poster_list[2])
#     with col4:
#         st.text(recommendations[3])
#         st.image(poster_list[3])
#     with col5:
#         st.text(recommendations[4])
#         st.image(poster_list[4])


# ----------------- Use native Streamlit button + show popcorn animation via components.html -----------------

animation_html = r"""
<style>

:root{ --gold:#FFD700; --btnColor:#0b0b0b; }
#animWrapper { display:flex; 
justify-content:center;
 align-items:center;
  height: 200px;      /* let it grow/shrink */
   }
.popcorn {
  position: absolute;
  font-size: 22px;
  pointer-events: none;
  will-change: transform, opacity;
}

@keyframes popMove {
  from { transform: translate(0,0) scale(1); opacity: 1; }
  to   { transform: translate(var(--x), var(--y)) scale(var(--s)); opacity: 0; }
}   
</style>

<div id="animWrapper"></div>
<div></div>

<script>
(function(){
  const container = document.getElementById("animWrapper");

  // create burst immediately when iframe loads
  function burst(count=18){
    let finished = 0; // track how many finished
    for (let i = 0; i < count; i++) {
      const el = document.createElement("div");
      el.className = "popcorn";
      el.textContent = "🍿";
      // center near middle
      el.style.left = (container.clientWidth/2) + "px";
      el.style.top  = (container.clientHeight/2) + "px";

      // random target
      const x = (Math.random() - 0.5) * (170 + Math.random()*150); // px
      const y = -Math.random() * (140 + Math.random()*120); // negative to go up more
      const s = 0.8 + Math.random()*1.1;

      el.style.setProperty("--x", x + "px");
      el.style.setProperty("--y", y + "px");
      el.style.setProperty("--s", s);

      // random rotation and delay
      const rot = (Math.random() - 0.5) * 80;
      el.style.transform = `translate(0,0) rotate(${rot}deg)`;

      // small random delay so pieces are slightly staggered
      const delay = Math.random() * 80; // ms
      el.style.opacity = "0.0";
      el.style.transition = `opacity 60ms ease ${delay}ms`;

      container.appendChild(el);

      // start animation slightly after insertion
      setTimeout(() => {
        el.style.opacity = "1";
        el.style.animation = `popMove 900ms cubic-bezier(.15,.8,.25,1) forwards`;
        el.style.transform = `translate(${x}px, ${y}px) rotate(${rot}deg)`;
      }, 20+delay);
      // stop animation slightly after insertion);

      // remove after animation
      setTimeout(()=> {
        el.remove();
        finished++;
        if(finished === count){ 
          // all elements are gone → shrink wrapper
          container.style.transition = "all 0.4s ease";
          container.style.width = "0px";
          container.style.height = "0px";
          container.style.overflow = "hidden";
        }
      }, 1150 + delay);
    }
    
  }

  // play burst on iframe load (so Python triggers the iframe after clicking)
  burst(18);
})();
</script>
"""

# Now use the regular Streamlit button.
if st.button("Recommend"):
    with st.spinner("Fetching your movie recommendations 🎞️..."):
    # run your recommender
        recommendations, poster_list = recommend(option)

        # show the popcorn animation (runs immediately inside its iframe)
        components.html(animation_html, height=180)


        # render results (your existing card markup)
        cols = st.columns(5)
        for idx, col in enumerate(cols):
            with col:
                st.markdown(
                    f"""
                    <div class="reco-card" style="padding:12px; border-radius:14px; background-color:rgba(30,30,30,0.95); text-align:center; box-shadow:2px 6px 18px rgba(0,0,0,0.45);">
                        <h4 style="color:#FFD700; margin:8px 0 10px 0; font-size:16px; min-height:44px; overflow:hidden;">{recommendations[idx]}</h4>
                        <img src="{poster_list[idx]}" style="border-radius:10px; width:100%; height:360px; object-fit:cover;">
                    </div>
                    """,
                    unsafe_allow_html=True
                )



    # Center the image using columns

st.markdown(
    """
    <style>
        .footer {
            font-size: 14px;
            color: #888888;  /* lighter gray text */
        }
        .footer img {
            width: 40px;   /* small profile picture */
            height: 40px;
            border-radius: 50%;  /* make it circular */
            margin-top: 5px;
        }
    </style>

    <br><hr>
    <div class="footer" style="text-align:center;">
    🚀 <b>Machine Learning Project</b> | 👨‍💻 Developed by <b>Swapnil Sengupta</b><br>
    🧠 Model: <i>Vectorization (Bag of Words) + NLP (nltk, sklearn)</i> <br>
    🎨 UI: <b>Streamlit</b> | 📊 Data Source: <i>TMDb</i>
    </div>

    """,
    unsafe_allow_html=True
)
col1, col2, col3 = st.columns([4, 1, 4])  # middle column is smaller
with col2:
    st.image("mypic.png", width=160)  # slightly bigger than before



