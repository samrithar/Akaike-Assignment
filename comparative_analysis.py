def comparative_analysis(articles):
    """
    Conduct comparative sentiment analysis across multiple articles.

    Args:
    articles (list): List of articles with sentiment labels.

    Returns:
    dict: A structured comparison of sentiment distribution.
    """
    sentiment_count = {"POSITIVE": 0, "NEGATIVE": 0, "NEUTRAL": 0}

    for article in articles:
        sentiment = article["sentiment"]
        if sentiment in sentiment_count:
            sentiment_count[sentiment] += 1

    # Generate insights
    insights = []
    if sentiment_count["POSITIVE"] > sentiment_count["NEGATIVE"]:
        insights.append("The majority of news articles are positive, indicating favorable media coverage.")
    elif sentiment_count["NEGATIVE"] > sentiment_count["POSITIVE"]:
        insights.append("The majority of news articles are negative, suggesting concerns or controversies.")
    else:
        insights.append("News coverage is balanced with mixed opinions.")

    # Identify common and unique topics
    common_topics = set()
    unique_topics = []

    for article in articles:
        if "topics" in article:
            article_topics = set(article["topics"])
            if common_topics:
                common_topics.intersection_update(article_topics)
            else:
                common_topics = article_topics
            unique_topics.append(article_topics)

    return {
        "Sentiment Distribution": sentiment_count,
        "Insights": insights,
        "Common Topics": list(common_topics),
        "Unique Topics": unique_topics,
    }
