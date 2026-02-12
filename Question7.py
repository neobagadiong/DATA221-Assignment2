from bs4 import BeautifulSoup
import requests

#declare variables needed to scrape wikipage
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 OPR/126.0.0.0 (Edition std-1)',
}
url = 'https://en.wikipedia.org/wiki/Data_science'

#scrape HTML from webpage
dataSciWikiHTML = BeautifulSoup(requests.get(url, headers=header).text , 'html.parser')
pTagsDataSci = dataSciWikiHTML.find('div',id='mw-content-text').find_all('p')

#print page title and first paragraph with more than 50 chars
print(dataSciWikiHTML.find('title').get_text())

for paragraph in pTagsDataSci:
    if len(paragraph.get_text().strip()) >= 50:
        print (paragraph.get_text())
        break 