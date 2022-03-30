from bs4 import BeautifulSoup
import pandas as pd
import json
import requests

pd.set_option('display.width', 400)  # Settings for view in Pycharm *ignore
pd.set_option('display.max_columns', 10)

# Read the file into a Python list object
with open('test.txt', 'r') as f:  # Imports list of art work links created in previous script
    list_links = json.loads(f.read())

list_links = [x for x in list_links if "?search" not in x]  # Eliminates duplicated links


list1 = list_links[0:10]  # Small part of the list just to make a sample, otherwise its running time is two long, also this list is duplicated
df = pd.DataFrame(columns=['Titles', 'Date', 'Author'])

for url in list1:
    content = requests.get(url).text
    soup = BeautifulSoup(content, "html.parser")
    new_row = {'Titles': soup.find('em').text, 'Date': soup.find('dd', attrs={'property': 'date:textDate'}),
               'Author': soup.find('span', attrs={'property': 'ecidoc:p131_E82_p102_has_title'})}  # Iterates over list to bring name of the art work.
    df = df.append(new_row, ignore_index=True)
df.drop_duplicates()
print(df)
df.to_csv(index=False)
