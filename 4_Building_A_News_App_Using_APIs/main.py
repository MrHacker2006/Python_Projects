import requests

query = input("Enter the topic, in which you are interested today: ")
api = "4959237c1b0d42e780524462f8c0cb59"

url = f"https://newsapi.org/v2/everything?q={query}&from=2025-07-17&to=2025-07-17&sortBy=popularity&apiKey={api}"

print(url)

r = requests.get(url)

data = r.json()

articles = data['articles']

for index, article in enumerate(articles): 
    print(index +1, article['title'], article['url'])
    print("\n ****************************** \n")