import requests

# r = requests.get("https://example.com")

# print(r.status_code)

# r.encoding = "ISO-8859-1"

# print(r.encoding)

# r = requests.get("https://api.github.com/events")




# data = r.json()

# print(data)

r = requests.get(
    "https://api.github.com/events",
    stream=True
)

print(r.raw)