import requests

API_KEY = "b77d3d2977a84de8aac38b50acb3c243"


def fetch_news(topic):

    url = (
        f"https://newsapi.org/v2/everything?"
        f"q={topic}&"
        f"language=en&"
        f"sortBy=publishedAt&"
        f"pageSize=15&"
        f"apiKey={API_KEY}"
    )

    response = requests.get(url)

    return response.json()