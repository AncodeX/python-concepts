import requests
from bs4 import BeautifulSoup

url = 'https://archive.ics.uci.edu/ml/datasets.php'

response = requests.get(url)
status = response.status_code
print(status)

content = response.content

soup = BeautifulSoup(content, "html.parser")

print(soup.title)
print(soup.title.get_text())

tables = soup.find_all('table', {'cellpadding':'3'})
table = tables[0] # the result is a list, we are taking out data from it
for td in table.find('tr').find_all('td'):
    print(td.text)

#print(soup.body)
#print(soup.head)