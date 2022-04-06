from bs4 import BeautifulSoup
import pandas as pd
import json
import requests
import time
import re
from time import sleep

pd.set_option('display.width', 400)  # Settings for view in Pycharm *ignore
pd.set_option('display.max_columns', 10)

# Read the file into a Python list object
with open('test.txt', 'r') as f:  # Imports list of art work links created in previous script
    list_links = json.loads(f.read())

list_links = [x for x in list_links if "?search" not in x]  # Eliminates duplicated links

list1 = list_links[0:10]   # Small part of the list just to make a sample, otherwise its running time is two long, also this list is duplicated
df = pd.DataFrame(columns=['ID', 'Titles', 'Date', 'Author', 'Technique','Height(cm)', 'Width(cm)','Series','Origin'])

chunks = [list1[x:x+10] for x in range(0, len(list1), 10)] # divide lista enlistas menores cambiar numeros para ejecutar lista completa
print(len(list1), len(list_links), len(chunks))

for element in chunks:
    time.sleep(10)
    print(1)
    for url in element:
        df1 = pd.DataFrame(columns=['ID', 'Titles', 'Date', 'Author', 'Technique', 'Height(cm)', 'Width(cm)', 'Series', 'Origin'])
        content = requests.get(url).text
        soup = BeautifulSoup(content, "html.parser")

        new_row = {'ID': soup.find('span', attrs={'property': 'cidoc:p102_has_title'}).text, 'Titles': soup.find('em').text, 'Date': soup.find('dd', attrs={'property': 'date:textDate'}).text,
                   'Author': soup.find('span', attrs={'property': 'ecidoc:p131_E82_p102_has_title'}).text,
                   'Technique': soup.find('span', attrs={'rel': 'ecidoc:p108i_E12_p32_used_general_technique'}).text, 'Height(cm)': soup.findAll('span', attrs={'about':  re.compile(r'http://museodelprado.es/items/E54_Dimension')})[2].text,
                   'Width(cm)': soup.findAll('span', attrs={'about': re.compile(r'http://museodelprado.es/items/E54_Dimension')})[6].text,
                   'Series':soup.find('dd', attrs={'property': 'ecidoc:p46i_E78_p102_forms_part_of'}),'Origin':soup.find('dd', attrs={'property': 'cidoc:p27_moved_from'}).text}  # Iterates over list to bring name of the art work.
        df = df.append(new_row, ignore_index=True)

df.drop_duplicates()
df.to_csv("art_data", ',')
print(df)
