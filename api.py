from flask import Flask, request, jsonify
from utils import fetch_news, analyze_sentiment, comparative_analysis, generate_tts

app = Flask(__name__)

@app.route("/fetch-news", methods=["GET"])
def get_news():
    company = request.args.get("company")
    articles = fetch_news(company)
    articles = analyze_sentiment(articles)
    analysis = comparative_analysis(articles)
    tts_file = generate_tts(f"Company {company} has {analysis['Sentiment Distribution']}", "summary.mp3")

    return jsonify({
        "company": company,
        "articles": articles,
        "comparative_analysis": analysis,
        "audio": tts_file
    })

if __name__ == "__main__":
    app.run(debug=True)

