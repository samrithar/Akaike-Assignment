import requests

API_KEY = 28d6a2c6208c400d84d3e303d9ec7158  # Replace with your actual API key

def extract_news(company):
    """
    Extracts news articles from NewsAPI related to the given company.
    Returns a list of dictionaries with title, summary, and URL.
    """
    url = f"https://newsapi.org/v2/everything?q={company}&language=en&apiKey={API_KEY}"

    response = requests.get(url)

    if response.status_code != 200:
        return {"error": "Failed to fetch news"}

    data = response.json()
    articles = []

    for item in data.get("articles", [])[:10]:  # Get first 10 articles
        articles.append({
            "title": item.get("title", "No Title"),
            "summary": item.get("description", "No Summary"),
            "url": item.get("url", "No URL")
        })

    return articles
