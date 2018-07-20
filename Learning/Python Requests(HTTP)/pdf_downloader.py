import requests #hhtp requests
import os #operating system functions

#Program downloads all PDF links from a given webpage
#Stores the downloaded pdfs in a new directory
####################################################################################
#Function extacts pdf titles and pdf links from html text
#reutrns list of tuples each element as (title, link)
def extractTitlesAndLinks(html):
    #This section extracts all contents of quotations and put them in a list
    listOfStringsFromQuotes = []
    tempStr = ""
    reading = False
    for char in html:
        if char=='"':
            reading = not reading
            #print("Reading On: " + reading)
            if reading == False:
                listOfStringsFromQuotes.append(tempStr)
                tempStr = ""
            continue
        if reading:
            tempStr += char
        #print("Current Char: " + char)
        #print("String currently building: " + tempStr)

    #section test print
    print(listOfStringsFromQuotes)

    #This section filters out all the strings that don't end in .PDF
    pdfLinks = list(filter(lambda x: x.endswith('.PDF'), listOfStringsFromQuotes))

    #section test print
    print(pdfLinks)

    #This section extracts the name of the pdf file for saving
    pdfLinks_withoutExtenstion = [x[:-4] for x in pdfLinks] #cut off .pdf
    pdfTitles = [x.split('/')[-1] for x in pdfLinks_withoutExtenstion] #take all after last '/'

    #section test print
    print(pdfTitles)

    #zip & reutrn
    return list(zip(pdfTitles, pdfLinks))
###########################################################################################



url = input('Please enter a valid website address: ')
directory = input('Please enter the directory name: ')

os.mkdir(directory)
os.chdir(directory)


try:
    mainResponse = requests.get(url)
except Exception:
    print("Something went wrong ensure correct website!")
    
titlesAndLinks = extractTitlesAndLinks(mainResponse.text)

for title, link in titlesAndLinks:
    response = requests.get(link)
    with open(title + '.pdf', 'wb') as f:
        f.write(response.content)
        f.close()
