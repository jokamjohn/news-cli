import requests


class NEWSAPI:

    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://newsapi.org/v2/"
        self.top_headlines_base_endpoint = "top-headlines"
        self.everything_endpoint = "everything"

    def get_top_headlines(self, country):
        url = self.base_url + self.top_headlines_base_endpoint + "?country=" + country + "&apikey=" + self.api_key
        request = requests.get(url)
        if request.status_code == 200:
            data = request.json()
            articles = data['articles']
            return articles
        return "An error occurred"
