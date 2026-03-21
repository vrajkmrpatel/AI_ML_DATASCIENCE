import requests as r

url = "https://api.quotable.io/random"

request: r.Response = r.get(url)
data: dict = request.json()

print(data)
print(f"{data['content']} - {data['author']}")