import requests

query = input("What type of news are you intrested in today? ")

api = "2b62786ca40448388b51be9881363e04"

url = f"https://newsapi.org/v2/everything?q={query}&from=2025-05-21&sortBy=publishedAt&apiKey={api}"

print(url)

r = requests.get(url)

data = r.json()
articles = data["articles"]

for index, article in enumerate(articles):
    print(index + 1, article["title"], article["url"])
    print("\n*******************************\n")