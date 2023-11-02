import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.hsx.vn/Modules/Listed/Web/Symbols?fid=9ac914fbe9434adca2801e30593d0ae2')
soup = BeautifulSoup(response.text, 'html.parser')
table = soup.find('table') # Assuming only one table or you can be more specific

for row in table.find_all('tr'):
    columns = row.find_all('td')
    if columns:
        stock_code = columns[0].text
        print(stock_code)
