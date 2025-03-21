from comparative_analysis import generate_sentiment_summary

# Sample articles for testing
articles = [
    {"title": "Tesla stock surges", "summary": "Tesla's stock reaches new highs.", "sentiment": "POSITIVE"},
    {"title": "Tesla faces lawsuit", "summary": "Tesla is under legal scrutiny for workplace violations.", "sentiment": "NEGATIVE"},
]

# Generate sentiment summary and TTS output
result = generate_sentiment_summary(articles)

# Print the summary and audio file location
print("Generated Sentiment Summary:\n", result["summary"])
print("Audio File:", result["audio"])
