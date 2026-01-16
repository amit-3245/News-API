import requests

query = input("Enter the topic you want to search news for: ")


api ="160ce53a98264252a0839d1c6110be0c"

url = f"https://newsapi.org/v2/everything?q={query}&from=2025-12-15&sortBy=publishedAt&apiKey={api}"

print(url)
r = requests.get(url)

data = r.json()
articles = data["articles"]

for index, article in enumerate(articles):
    print(index + 1,article["title"], article["url"])
    print("\n*******************************\n")

