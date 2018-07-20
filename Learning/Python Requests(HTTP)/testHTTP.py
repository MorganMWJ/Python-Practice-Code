import requests
url = "https://www.wikipedia.org/"
r = requests.get(url)
print(r.text)
