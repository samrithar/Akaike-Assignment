from sentiment_analysis import analyze_sentiment

# Sample test data
articles = [
    {"title": "Tesla profits hit record high", "summary": "Tesla has reported a record-breaking profit this quarter."},
    {"title": "Tesla faces safety investigation", "summary": "Government agencies are investigating Tesla's autopilot system after multiple crashes."}
]

# Perform sentiment analysis
analyzed_articles = analyze_sentiment(articles)

# Print results
for article in analyzed_articles:
    print(f"Title: {article['title']}")
    print(f"Summary: {article['summary']}")
    print(f"Sentiment: {article['sentiment']}\n")
