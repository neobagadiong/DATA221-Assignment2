from bs4 import BeautifulSoup
import requests
import pandas

#declare variables needed to scrape wikipage
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 OPR/126.0.0.0 (Edition std-1)',
}
url = 'https://en.wikipedia.org/wiki/Machine_learning'

#pull webpage as HTML
machineLearningWikiHTML = BeautifulSoup(requests.get(url, headers=header).text , 'html.parser')
machineLearningWikiTables = machineLearningWikiHTML.find('div',id='mw-content-text').find_all('table')
firstThreeColumnTable = None

#find first table with rows with more than 3 "columns"
for table in machineLearningWikiTables:
    firstRow = table.find('ul')
    columns = firstRow.find_all(['th','td','li'])
    if len(columns) >= 3:
        firstThreeColumnTable = table
        break

HTMLtableToList =[]

#formatted to follow the given example output csv
for row in firstThreeColumnTable.find_all('tr'):    
    rowText = row.get_text().replace('\n',' ')
    if rowText[0] == ' ': 
        HTMLtableToList.append(rowText[1:])
    else:
        HTMLtableToList.append(rowText)

#output a csv 
wikiHTMLDataFrame = pandas.DataFrame(HTMLtableToList)
wikiHTMLDataFrame.to_csv('wiki_table.csv',index=False,header=False)