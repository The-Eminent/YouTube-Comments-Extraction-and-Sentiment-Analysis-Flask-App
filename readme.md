# YouTube Comments Sentiment Analysis Flask App

A web application built with Python Flask that extracts comments from a YouTube video and performs sentiment analysis to classify comments as Positive, Negative, or Neutral. The results are displayed in an interactive pie chart, along with sample comments for each sentiment.

## Features
- **YouTube Comments Extraction**: Fetches comments from any YouTube video using the YouTube Data API.
- **Sentiment Analysis**: Analyzes the sentiment of comments using TextBlob.
- **Interactive Visualization**: Displays sentiment analysis results in a pie chart using Chart.js.
- **Sample Comments**: Shows 5-10 sample comments for each sentiment (Positive, Negative, Neutral).
- **User-Friendly UI**: Built with Bootstrap for a clean and responsive design.

## Technologies Used
- **Backend**: Python (Flask, TextBlob, Requests)
- **Frontend**: HTML, CSS, JavaScript, Bootstrap, Chart.js
- **APIs**: YouTube Data API v3

## Setup Instructions

### Prerequisites
1. **Python 3.x**: Install Python from [python.org](https://www.python.org/).
2. **YouTube Data API Key**: Get your API key from the Google Cloud Console.

### Installation

1. **Clone the repository**:
git clone [https://github.com/The-Eminent/youtube-sentiment-analysis.git](https://github.com/The-Eminent/YouTube-Comments-Extraction-and-Sentiment-Analysis-Flask-App.git)
cd youtube-sentiment-analysis

2. **Create a virtual environment**:
python -m venv venv

3. **Activate the virtual environment**:
- On Windows:
  ```
  venv\Scripts\activate
  ```
- On macOS/Linux:
  ```
  source venv/bin/activate
  ```

4. **Install dependencies**:
pip install -r requirements.txt

5. **Set up environment variables**:
- Create a `.env` file in the root directory.
- Add your YouTube Data API key:
  ```
  YOUTUBE_API_KEY=your_api_key_here
  ```

6. **Run the application**:
python app.py

7. Open your browser and go to [http://127.0.0.1:5000](http://127.0.0.1:5000).

