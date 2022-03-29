from bs4 import BeautifulSoup
import pandas as pd
import json
import requests

#Now read the file back into a Python list object
with open('test.txt', 'r') as f:
    list = json.loads(f.read())

list1 = list[0:10]
print(list1)
df = pd.DataFrame()

for url in list1:
# def getInfo(URL):
      content = requests.get(url).text
      soup = BeautifulSoup(content, "html.parser")
      print(soup.find('em'))
