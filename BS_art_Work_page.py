from bs4 import BeautifulSoup
import pandas as pd
import json
import requests

#Now read the file back into a Python list object
with open('test.txt', 'r') as f:
    list = json.loads(f.read())

for url in list:
# def getInfo(URL):
      content = requests.get(url).text
      soup = BeautifulSoup(content, "html.parser")
      print(soup.body.h1)
#
#
# #df = pd.DataFrame()
# for i in list:
#     print(getInfo(i))

