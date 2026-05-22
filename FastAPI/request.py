# import requests

# r = requests.get("https://api.github.com/events")

# print(r)


import requests

data = {
    "name": "Pallavi",
    "age": 20
}

# r = requests.post(
#     "https://httpbin.org/post",
#     data=data
# )

# print(r.text)

# r = requests.put(
#     "https://httpbin.org/put",
#     data={"name": "Updated"}
# )

# print(r.text)

# URL PARAMETERS
# r = requests.head("https://httpbin.org/get")

# print(r.headers)

# payload = {
#     "id": 10,
#     "name": "ram"
# }

# r = requests.get(
#     "https://httpbin.org/get",
#     params=payload
# )

# print(r.url)

r.encoding = "ISO-8859-1"
print(r.encoding)