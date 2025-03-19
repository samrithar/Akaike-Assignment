import requests
from bs4 import BeautifulSoup
from newspaper import Article
import nltk
nltk.download('punkt')

from transformers import pipeline
from gtts import gTTS
import pandas as pd

# Sentiment model
sentiment_model = pipeline("sentiment-analysis")

def fetch_news(company_name):
    search_url = f"https://news.google.com/search?q={company_name}"
    response = requests.get(search_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    links = [a['href'] for a in soup.find_all('a', href=True) if 'articles' in a['href']]
    articles = []

    for link in links[:10]:
        full_link = f"https://news.google.com{link}"
        article = Article(full_link)
        article.download()
        article.parse()
        article.nlp()

        articles.append({
            "title": article.title,
            "summary": article.summary,
            "content": article.text
        })

    return articles

def analyze_sentiment(articles):
    for article in articles:
        result = sentiment_model(article["summary"])[0]
        article["sentiment"] = result["label"]
    return articles

def comparative_analysis(articles):
    df = pd.DataFrame(articles)
    sentiment_counts = df["sentiment"].value_counts().to_dict()
    
    return {
        "Sentiment Distribution": sentiment_counts,
        "Positive Articles": df[df["sentiment"] == "POSITIVE"].to_dict(orient="records"),
        "Negative Articles": df[df["sentiment"] == "NEGATIVE"].to_dict(orient="records"),
    }

def generate_tts(summary, filename="output.mp3"):
    tts = gTTS(summary, lang="hi")
    tts.save(filename)
    return filename

