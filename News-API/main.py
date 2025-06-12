import requests

print("\nWELCOME TO API NEWS\n")
query = input("What type of news you want ?\n")
api = "bc6f5e25027a481c894b06ab24f281b4"

url = f"https://newsapi.org/v2/everything?q={query}&from=2025-06-11&to=2025-06-11&sortBy=popularity&apiKey={api}"

r = requests.get(url)
data = r.json()
articles = data["articles"]

for article in articles:
    print("TITLE: ",article["title"],"\n","FOR MORE CLICK ON URL: ", article["url"])
    print("\n-------------------------------------------------------------------------------\n")

print("<----  THANKS FOR USING  ---->")    