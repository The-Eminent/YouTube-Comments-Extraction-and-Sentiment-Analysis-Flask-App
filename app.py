from flask import Flask, render_template, request, redirect, url_for
import requests
from textblob import TextBlob
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

app = Flask(__name__)

# YouTube Data API settings
YOUTUBE_API_KEY = os.getenv('YOUTUBE_API_KEY')
YOUTUBE_API_URL = 'https://www.googleapis.com/youtube/v3/commentThreads'

def get_video_id(url):
    """Extract video ID from YouTube URL."""
    if 'v=' in url:
        return url.split('v=')[1].split('&')[0]
    return None

def get_comments(video_id):
    """Fetch comments from YouTube video using YouTube Data API."""
    params = {
        'part': 'snippet',
        'videoId': video_id,
        'key': YOUTUBE_API_KEY,
        'maxResults': 100  # Adjust as needed
    }
    response = requests.get(YOUTUBE_API_URL, params=params)
    if response.status_code != 200:
        return []
    data = response.json()
    comments = [item['snippet']['topLevelComment']['snippet']['textDisplay'] for item in data['items']]
    return comments

def analyze_sentiment(comments):
    """Analyze sentiment of comments using TextBlob."""
    sentiments = []
    for comment in comments:
        analysis = TextBlob(comment)
        polarity = analysis.sentiment.polarity
        if polarity > 0:
            sentiments.append('Positive')
        elif polarity < 0:
            sentiments.append('Negative')
        else:
            sentiments.append('Neutral')
    return sentiments

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    video_url = request.form['video_url']
    video_id = get_video_id(video_url)
    if not video_id:
        return render_template('index.html', error="Invalid YouTube URL")

    comments = get_comments(video_id)
    if not comments:
        return render_template('index.html', error="No comments found or API limit exceeded")

    sentiments = analyze_sentiment(comments)
    sentiment_counts = {
        'Positive': sentiments.count('Positive'),
        'Negative': sentiments.count('Negative'),
        'Neutral': sentiments.count('Neutral')
    }

    # Get sample comments for each sentiment
    sample_positive = [comment for comment, sentiment in zip(comments, sentiments) if sentiment == 'Positive'][:10]
    sample_negative = [comment for comment, sentiment in zip(comments, sentiments) if sentiment == 'Negative'][:10]
    sample_neutral = [comment for comment, sentiment in zip(comments, sentiments) if sentiment == 'Neutral'][:10]

    return render_template(
        'results.html',
        video_url=video_url,
        sentiment_counts=sentiment_counts,
        total_comments=len(comments),
        sample_positive=sample_positive,
        sample_negative=sample_negative,
        sample_neutral=sample_neutral
    )

if __name__ == '__main__':
    app.run(debug=True)