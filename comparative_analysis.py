from text_to_speech import text_to_speech

def generate_sentiment_summary(articles):
    """
    Generate a Hindi summary based on the sentiment analysis results and convert to speech.

    Args:
    articles (list): List of articles with sentiment labels.

    Returns:
    dict: Summary text and audio file path.
    """
    sentiment_result = comparative_analysis(articles)
    
    # Generate Hindi summary text
    sentiment_text = "कंपनी की खबरें इस प्रकार हैं:\n"
    sentiment_text += f"सकारात्मक खबरें: {sentiment_result['Sentiment Distribution']['POSITIVE']}\n"
    sentiment_text += f"नकारात्मक खबरें: {sentiment_result['Sentiment Distribution']['NEGATIVE']}\n"
    sentiment_text += f"तटस्थ खबरें: {sentiment_result['Sentiment Distribution']['NEUTRAL']}\n"

    if sentiment_result["Insights"]:
        sentiment_text += f"निष्कर्ष: {sentiment_result['Insights'][0]}\n"

    # Convert text to speech
    audio_file = text_to_speech(sentiment_text)

    return {"summary": sentiment_text, "audio": audio_file}
