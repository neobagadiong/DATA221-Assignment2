from bs4 import BeautifulSoup
import requests, csv


header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 OPR/126.0.0.0 (Edition std-1)',
}
url = 'https://en.wikipedia.org/wiki/Machine_learning'

machineLearningWikiHTML = BeautifulSoup(requests.get(url, headers=header).text , 'html.parser')

machineLarning = machineLearningWikiHTML.find(id='mw-content-text').find_('table')





print(rosterTable)

