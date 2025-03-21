from transformers import pipeline

# Load sentiment analysis pipeline
sentiment_pipeline = pipeline("sentiment-analysis")

def analyze_sentiment(articles):
    """
    Perform sentiment analysis on a list of articles.
    
    Args:
    articles (list): List of articles, where each article is a dictionary with a 'summary' key.

    Returns:
    list: Articles with an added 'sentiment' key.
    """
    for article in articles:
        sentiment_result = sentiment_pipeline(article['summary'])[0]
        article['sentiment'] = sentiment_result['label']
    return articles
