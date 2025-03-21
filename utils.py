import requests
from bs4 import BeautifulSoup

def extract_news(company):
    """
    Extracts news articles related to the given company from Google News.
    Returns a list of dictionaries containing title and summary.
    """
    url = f"https://news.google.com/search?q={company}"
    headers = {'User-Agent': 'Mozilla/5.0'}  # To prevent blocking

    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        return {"error": "Failed to fetch news"}

    soup = BeautifulSoup(response.text, 'html.parser')

    articles = []
    for item in soup.select('article')[:10]:  # Extract up to 10 articles
        title = item.find('h3')
        summary = item.find('p')

        article_data = {
            'title': title.text if title else 'No Title',
            'summary': summary.text if summary else 'No Summary'
        }

        articles.append(article_data)
    
    return articles
