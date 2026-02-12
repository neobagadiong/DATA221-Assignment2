from bs4 import BeautifulSoup
import requests

#declare variables needed to scrape wikipage
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 OPR/126.0.0.0 (Edition std-1)',
}
url = 'https://en.wikipedia.org/wiki/Data_science'

#scrape HTML from webpage
dataSciWikiHTML = BeautifulSoup(requests.get(url, headers=header).text , 'html.parser')
h2TagsDataSci = dataSciWikiHTML.find('div',id='mw-content-text').find_all('h2')

#creates textfile
headingsTextFile = open("headings.txt", "w")

#writes lines to text file if it isnt 'References', 'External links', 'See also',or 'Notes'
for header in h2TagsDataSci:
    if header.get_text() not in ['References', 'External links', 'See also','Notes']:
        headingsTextFile.write(header.get_text()+'\n')

