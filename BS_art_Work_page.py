from bs4 import BeautifulSoup
import pandas as pd
import json
import requests

#Now read the file back into a Python list object
with open('test.txt', 'r') as f:
    list = json.loads(f.read())

df = pd.DataFrame()

for url in list:
# def getInfo(URL):
      content = requests.get(url).text
      soup = BeautifulSoup(content, "html.parser")
      x = soup.find('em')
      df.append(pd.DataFrame(x))

print(df.head(50))