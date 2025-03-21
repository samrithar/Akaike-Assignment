from comparative_analysis import comparative_analysis

# Sample data
articles = [
    {"title": "Tesla reaches new highs", "summary": "Tesla's stock is soaring.", "sentiment": "POSITIVE", "topics": ["Stock Market", "Innovation"]},
    {"title": "Tesla faces safety issues", "summary": "Tesla is under investigation for self-driving issues.", "sentiment": "NEGATIVE", "topics": ["Regulations", "Autonomous Vehicles"]},
    {"title": "Tesla expands globally", "summary": "Tesla announces new factories worldwide.", "sentiment": "POSITIVE", "topics": ["Expansion", "Global Market"]},
]

# Perform comparative analysis
comparison_result = comparative_analysis(articles)

# Print results
print(comparison_result)
