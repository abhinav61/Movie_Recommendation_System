# Due to the large size of the calculate_similarity.pkl , I have not uploaded the file. Please mail me at abhinavk806@gmail.com for the file

# Movie Recommendation System

A content-based movie recommendation system built with Python and Streamlit that suggests movies based on user preferences using machine learning techniques.

## Project Purpose

The purpose of this project is to build an intelligent movie recommendation system that can:
- Analyze movie content and features to find similar movies
- Provide personalized movie recommendations based on user selection
- Display movie posters fetched from TMDB API for better user experience
- Demonstrate practical application of machine learning in recommendation systems by creating the model and using the model in the application

## Features

- **Content-Based Filtering**: Uses movie features like genres, cast, crew, and keywords
- **Interactive Web Interface**: Built with Streamlit for easy user interaction
- **Movie Poster Integration**: Fetches movie posters from TMDB API
- **Real-time Recommendations**: Provides 5 similar movie recommendations instantly
- **User-Friendly Interface**: Clean and intuitive design with movie posters and titles

## Technology Stack

- **Python**: Core programming language
- **Streamlit**: Web application framework
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computing
- **Scikit-learn**: Machine learning library
- **NLTK**: Natural language processing
- **Requests**: HTTP library for API calls
- **Pickle**: Data serialization


## Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/movie-recommendation-system.git
cd movie-recommendation-system
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Download NLTK Data
```python
import nltk
nltk.download('punkt')
nltk.download('stopwords')
```

### 5. Get TMDB API Key
1. Visit [TMDB API](https://www.themoviedb.org/settings/api)
2. Create an account and get your API key
3. Replace the Bearer token in `app.py` with your API key

### 6. Prepare Data Files
Ensure you have the following files/models in your project directory:
- `movies_list.pkl` - Processed movie dataset
- `calculate_similarity.pkl` - Similarity matrix

## Data Processing Steps

### 1. Data Collection
- Use TMDB 5000 Movie Dataset containing from kaggle:
  - Movie titles, genres, cast, crew
  - Keywords, overview, and metadata

### 2. Data Preprocessing
- Extract features from JSON-like strings for cast, crew, and genres
- Process movie overviews and keywords
- Clean and normalize text data

### 3. Feature Engineering
- Combine overview, genres, cast, keywords, and crew into tags
- Apply text preprocessing (stemming, lowercase conversion)
- Create feature vectors using CountVectorizer

### 4. Similarity Calculation
- Use CountVectorizer to convert text to numerical features
- Calculate cosine similarity between movie vectors
- Store similarity matrix for fast recommendations

## Usage

### 1. Run the Application
```bash
streamlit run app.py
```

### 2. Using the Interface
1. Select a movie from the dropdown menu
2. Click the "Recommend" button
3. View 5 similar movie recommendations with posters

### 3. Project Structure
```
movie-recommendation-system/
├── app.py                 # Main Streamlit application
├── movie_recommendations.ipynb  # Data processing notebook
├── movies_list.pkl        # Processed movie dataset
├── calculate_similarity.pkl  # Similarity matrix
├── requirements.txt       # Project dependencies
└── README.md             # Project documentation
```

## Deployment Options

### Option 1: Streamlit Cloud (Recommended)

1. **Push to GitHub**:
   ```bash
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

2. **Deploy on Streamlit Cloud**:
   - Visit [share.streamlit.io](https://share.streamlit.io)
   - Connect your GitHub account
   - Select your repository
   - Set main file path: `app.py`
   - Click "Deploy"

3. **Environment Setup**:
   - Add your TMDB API key in Streamlit Cloud secrets
   - Go to App settings → Secrets
   - Add: `TMDB_API_KEY = "your_api_key_here"`

### Option 2: Heroku Deployment

1. **Create Heroku Files**:

   Create `Procfile`:
   ```
   web: streamlit run app.py --server.port=$PORT --server.address=0.0.0.0
   ```

   Create `setup.sh`:
   ```bash
   mkdir -p ~/.streamlit/
   echo "\
   [general]\n\
   email = \"your-email@domain.com\"\n\
   " > ~/.streamlit/credentials.toml
   echo "\
   [server]\n\
   headless = true\n\
   enableCORS=false\n\
   port = $PORT\n\
   " > ~/.streamlit/config.toml
   ```

2. **Deploy to Heroku**:
   ```bash
   # Install Heroku CLI
   heroku login
   heroku create your-app-name
   git add .
   git commit -m "Deploy to Heroku"
   git push heroku main
   ```

3. **Set Environment Variables**:
   ```bash
   heroku config:set TMDB_API_KEY="your_api_key_here"
   ```

### Option 3: AWS EC2 Deployment

1. **Launch EC2 Instance**:
   - Choose Ubuntu Server 20.04 LTS
   - Configure security group (port 8501 for Streamlit)
   - Create and download key pair

2. **Connect to EC2**:
   ```bash
   ssh -i your-key.pem ubuntu@your-ec2-ip
   ```

3. **Setup Environment**:
   ```bash
   sudo apt update
   sudo apt install python3-pip
   pip3 install -r requirements.txt
   ```

4. **Run Application**:
   ```bash
   streamlit run app.py --server.port=8501 --server.address=0.0.0.0
   ```

5. **Keep App Running** (using screen):
   ```bash
   screen -S movie-app
   streamlit run app.py --server.port=8501 --server.address=0.0.0.0
   # Press Ctrl+A then D to detach
   ```

### Option 4: Google Cloud Platform (GCP)

1. **Create App Engine Configuration** (`app.yaml`):
   ```yaml
   runtime: python39
   
   env_variables:
     TMDB_API_KEY: "your_api_key_here"
   
   automatic_scaling:
     min_instances: 1
     max_instances: 10
   ```

2. **Deploy to GCP**:
   ```bash
   gcloud app deploy
   ```

### Option 5: DigitalOcean App Platform

1. **Create `requirements.txt`** (already done)

2. **Deploy via GitHub**:
   - Connect your GitHub repository
   - Set build command: `pip install -r requirements.txt`
   - Set run command: `streamlit run app.py --server.port=$PORT --server.address=0.0.0.0`

3. **Set Environment Variables**:
   - Add `TMDB_API_KEY` in app settings

## How It Works

1. **Content Analysis**: The system analyzes movie content including:
   - Genres (Action, Comedy, Drama, etc.)
   - Cast members (top 3 actors)
   - Director information
   - Keywords and plot overview

2. **Feature Extraction**: 
   - Combines all features into a single "tags" column
   - Applies text preprocessing (stemming, cleaning)
   - Creates numerical vectors using CountVectorizer

3. **Similarity Calculation**:
   - Uses cosine similarity to find similar movies
   - Calculates similarity scores between all movies
   - Stores similarity matrix for fast recommendations

4. **Recommendation Generation**:
   - Finds the selected movie's index
   - Retrieves similarity scores for all other movies
   - Returns top 5 most similar movies

## Performance Metrics

- **Response Time**: < 2 seconds for recommendations
- **Accuracy**: Content-based filtering ensures relevant recommendations
- **Coverage**: Supports 5000+ movies from TMDB dataset
- **Scalability**: Can be extended with more sophisticated algorithms

##  Future Enhancements

- [ ] Implement collaborative filtering
- [ ] Add user rating systems
- [ ] Include movie trailers and reviews
- [ ] Deploy on cloud platform (Heroku, AWS)
- [ ] Add more filtering options (year, rating, genre)
- [ ] Implement hybrid recommendation approach

## Acknowledgments

- [TMDB API](https://www.themoviedb.org/documentation/api) for movie data and posters
- [Kaggle TMDB Dataset](https://www.kaggle.com/tmdb/tmdb-movie-metadata) for training data
- Streamlit team for the amazing web framework

