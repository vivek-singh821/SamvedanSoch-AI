from textblob import TextBlob


def analyze_sentiment(text):

    if not text:
        return "Neutral", 0

    blob = TextBlob(text)

    polarity = blob.sentiment.polarity

    if polarity > 0:
        sentiment = "Positive"

    elif polarity < 0:
        sentiment = "Negative"

    else:
        sentiment = "Neutral"

    return sentiment, polarity