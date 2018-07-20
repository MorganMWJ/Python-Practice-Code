import requests

url = 'http://filestore.aqa.org.uk/resources/computing/AQA-75171-SQP-ADD.PDF'

response = requests.get(url)

with open('example.pdf', 'wb') as f:
    f.write(response.content)
