from bs4 import BeautifulSoup
import pandas as pd
import json
import requests

#Now read the file back into a Python list object
with open('test.txt', 'r') as f: #imports list of art work links created in previous script
    list = json.loads(f.read())
#pending remove duplicates
list1 = list[0:10] # small part of the list just to make a sample, otherwise its running time is two long, also this list is duplicated
df = pd.DataFrame()

for url in list1:
# def getInfo(URL):
      content = requests.get(url).text
      soup = BeautifulSoup(content, "html.parser")
      print(soup.find('em')) #iterates over list to bring name of the art work.
