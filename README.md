# Twitter Sentiment Analysis

## Overview
This project is a web-based Twitter Sentiment Analysis application developed using Python and Flask. It enables users to analyze the sentiment of tweets from Twitter users or manually entered text. The application preprocesses the data, performs sentiment analysis, and categorizes tweets into sentiment categories such as 'Strongly Negative,' 'Fairly Negative,' 'Neutral,' 'Fairly Positive,' or 'Strongly Positive.'

## Key Features
- Data preprocessing to clean and prepare text data.
- Sentiment analysis using the TextBlob library.
- An intuitive web interface built with Flask for user interactions.
- Integration with the Twitter API through Tweepy for tweet retrieval.
- Effective handling of challenges including API rate limits and ethical data usage.

## Project Structure
- `app.py`: The main Python script for the Flask web application.
- `templates/`: Directory containing HTML templates for web pages.
- `static/`: Directory for storing static assets like CSS and images.
- `requirements.txt`: List of project dependencies.
- `LICENSE`: Project license details.
- `README.md`: Project documentation.

## Getting Started
1. Clone this repository: `git clone https://github.com/yourusername/twitter-sentiment-analysis.git`
2. Install the required packages: `pip install -r requirements.txt`
3. Run the Flask application: `python app.py`
4. Access the application in your web browser at `http://localhost:5000`

## Usage
- To analyze tweets from a Twitter user, provide the username and tweet count on the homepage.
- To perform manual tweet analysis, enter the text in the provided text area.

## Future Enhancements
- Real-time sentiment analysis.
- Implementation of advanced sentiment categorization models.
- Enhanced data visualization for richer user experience.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- The project makes use of the [TextBlob](https://textblob.readthedocs.io/) library for sentiment analysis.
- Twitter data is retrieved using the [Tweepy](https://www.tweepy.org/) library.
