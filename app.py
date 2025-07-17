import streamlit as st
import pickle
import requests

def search_movie_by_title(title):
    """Search for a movie by title and return its TMDB ID"""
    url = f"https://api.themoviedb.org/3/search/movie?query={title}&language=en-US"
    
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer <your_aauth_key_here>"  # Replace with your actual API key
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        
        if data['results']:
            return data['results'][0]['id']  # Return first result's ID
        else:
            return None
            
    except requests.exceptions.RequestException as e:
        st.error(f"Error searching for movie: {e}")
        return None

def fetch_poster(movie_id):
    """Fetch poster using TMDB movie ID"""
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?language=en-US"
    
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer <your_aauth_key_here>"  # Replace with your actual API key
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        
        poster_path = data.get('poster_path')
        if poster_path:
            full_poster_url = f"https://image.tmdb.org/t/p/w500{poster_path}"
            return full_poster_url
        else:
            return None
            
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching poster: {e}")
        return None
    except KeyError:
        st.error("Poster not found in API response")
        return None

def fetch_poster_by_title(title):
    """Fetch poster by searching for movie title first"""
    movie_id = search_movie_by_title(title)
    if movie_id:
        return fetch_poster(movie_id)
    return None

# Load the full dataframe
movies_df = pickle.load(open('movies_list.pkl', 'rb'))
movies_list = movies_df['title'].values

similarity = pickle.load(open('calculate_similarity.pkl', 'rb'))

def recommend(movie):
    movie_index = movies_df[movies_df['title'] == movie].index[0]
    distance = similarity[movie_index]
    similar_movies = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6] 
    
    recommended_movies_posters = []
    recommended_movies = []
    
    for i in similar_movies:
        # Get movie title
        title = movies_df.iloc[i[0]].title
        recommended_movies.append(title)
        
        # Fetch poster by searching for the title
        poster = fetch_poster_by_title(title)
        recommended_movies_posters.append(poster)

    return recommended_movies, recommended_movies_posters

st.title("Movie Recommendation System")

option = st.selectbox('Select a movie you like:', movies_list)

if st.button('Recommend'):
    names, posters = recommend(option)

    # Display recommendations in columns
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.text(names[0])
        if posters[0]:
            st.image(posters[0])
        else:
            st.text("No poster available")
            
    with col2:
        st.text(names[1])
        if posters[1]:
            st.image(posters[1])
        else:
            st.text("No poster available")

    with col3:
        st.text(names[2])
        if posters[2]:
            st.image(posters[2])
        else:
            st.text("No poster available")
            
    with col4:
        st.text(names[3])
        if posters[3]:
            st.image(posters[3])
        else:
            st.text("No poster available")
            
    with col5:
        st.text(names[4])
        if posters[4]:
            st.image(posters[4])
        else:
            st.text("No poster available")