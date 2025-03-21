import requests
from bs4 import BeautifulSoup

def extract_news(company):
    url = f"https://news.google.com/search?q={company}"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    articles = []
    for item in soup.select('article')[:10]:  # Get first 10 articles
        title = item.find('h3').text if item.find('h3') else 'No Title'
        summary = item.find('p').text if item.find('p') else 'No Summary'
        articles.append({'title': title, 'summary': summary})
    
    return articles

print(extract_news("Tesla"))
