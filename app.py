from flask import Flask, render_template, request

from fetch_news import fetch_news
from analysis import analyze_sentiment
from clustering import cluster_articles

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():

    clusters_data = []

    if request.method == 'POST':

        topic = request.form['topic']

        data = fetch_news(topic)

        articles = data.get('articles', [])

        clean_articles = []

        for article in articles:

            news = {
                "title": article.get("title", "No Title"),
                "source": article.get("source", {}).get("name", "Unknown"),
                "description": article.get("description", "No Description")
            }

            clean_articles.append(news)

        clusters = cluster_articles(clean_articles)

        for cluster_id, cluster in enumerate(clusters, start=1):

            cluster_news = []

            sentiments = []

            for index in cluster:

                news = clean_articles[index]

                text = news['title'] + ' ' + str(news['description'])

                sentiment, polarity = analyze_sentiment(text)

                sentiments.append(sentiment)

                cluster_news.append({
                    'title': news['title'],
                    'source': news['source'],
                    'description': news['description'],
                    'sentiment': sentiment,
                    'polarity': round(polarity, 2)
                })

            bias = False

            if len(set(sentiments)) > 1:
                bias = True

            clusters_data.append({
                'cluster_id': cluster_id,
                'articles': cluster_news,
                'bias': bias
            })

    return render_template('index.html', clusters=clusters_data)


if __name__ == '__main__':
    app.run(debug=True)