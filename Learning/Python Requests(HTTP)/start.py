import requests

#test = requests.get('http://www.hipstercode.com')
#print(type(test))
#print(str(test.text.encode('utf-8')))

listOfLinks = ["http://www.hipstercode.com",
                "http://www.hipstercode.com/about/"]

for index, link in enumerate(listOfLinks):
    response = requests.get(link)
    outfile = open('testOutput' + str(index+1) + '.txt','w')
    response.encoding = 'ISO-8859-1'
    outfile.write(str(response.text))
    print(response.headers)
    print(response.cookies.get_dict())


'''
googleLink = "http://www.google.com"
payload = {'q': 'test'}
googleResponse = requests.get(googleLink, params = payload)
googleResponse.encoding = 'ISO-8859-1'
print(googleResponse.url)
'''
