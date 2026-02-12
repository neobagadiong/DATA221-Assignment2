from bs4 import BeautifulSoup
import requests, csv
import pandas

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 OPR/126.0.0.0 (Edition std-1)',
}
url = 'https://en.wikipedia.org/wiki/Machine_learning'


machineLearningWikiHTML = BeautifulSoup(requests.get(url, headers=header).text , 'html.parser')

rosterTable = machineLearningWikiHTML.find('div',id='mw-content-text').find_all('table')

print(rosterTable)

firstThreeColumnTable = None

for table in rosterTable:
    firstRow = table.find('ul')

    columns = firstRow.find_all(['th','td','li'])

    if len(columns) >= 3:
        firstThreeColumnTable = table
        break



HTMLtableToList =[]

for row in firstThreeColumnTable.find_all('tr'):
    
    rowText = row.get_text().replace('\n',' ')
    
    if rowText[0] == ' ': 
        HTMLtableToList.append(rowText[1:])
    else:
        HTMLtableToList.append(rowText)

wikiHTMLDataFrame = pandas.DataFrame(HTMLtableToList)
wikiHTMLDataFrame.to_csv('wiki_table.csv',index=False,header=False)

