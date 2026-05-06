from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def cluster_articles(articles):

    texts = []

    for article in articles:

        text = article['title'] + ' ' + str(article['description'])

        texts.append(text)

    vectorizer = TfidfVectorizer(stop_words='english')

    tfidf_matrix = vectorizer.fit_transform(texts)

    similarity_matrix = cosine_similarity(tfidf_matrix)

    clusters = []

    visited = set()

    threshold = 0.3

    for i in range(len(texts)):

        if i in visited:
            continue

        cluster = [i]

        visited.add(i)

        for j in range(i + 1, len(texts)):

            if similarity_matrix[i][j] > threshold:

                cluster.append(j)

                visited.add(j)

        clusters.append(cluster)

    return clusters