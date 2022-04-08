from bs4 import BeautifulSoup
import pandas as pd
import json
import requests
import time
import re

# Read the file into a Python list object
with open('Links.txt', 'r') as f:  # Imports list of art work links created in previous script
    list_links = json.loads(f.read())


# Create dataframe to store the data
df = pd.DataFrame(columns=['ID', 'Titles', 'Date', 'Author', 'Technique', 'Height(cm)', 'Width(cm)', 'Series', 'Origin', 'Support'])

# Divides the main list of links in smaller lists

chunks = [list_links[x:x+400] for x in range(0, len(list_links), 400)]
print(len(list_links), len(chunks))  # print number of total links and how many sub-lists were created

# Iterates over each list and sleeps for 10 seconds after each iteration
for element in chunks:
    time.sleep(10)
    for url in element:
        try:  # Exception Handling

            content = requests.get(url).text
            soup = BeautifulSoup(content, "html.parser")

            # After parsing the page it extracts all information from each art work using the tags below

            new_row = {'ID': soup.find('span', attrs={'property': 'cidoc:p102_has_title'}).text, 'Titles': soup.find('em').text, 'Date': soup.find('dd', attrs={'property': 'date:textDate'}).text,
                       'Author': soup.find('span', attrs={'property': 'ecidoc:p131_E82_p102_has_title'}).text,
                       'Technique': soup.find('span', attrs={'rel': 'ecidoc:p108i_E12_p32_used_general_technique'}).text, 'Height(cm)': soup.findAll('span', attrs={'about':  re.compile(r'http://museodelprado.es/items/E54_Dimension')})[2].text,
                       'Width(cm)': soup.findAll('span', attrs={'about': re.compile(r'http://museodelprado.es/items/E54_Dimension')})[6].text,
                       'Series': soup.find('dd', attrs={'property': 'ecidoc:p46i_E78_p102_forms_part_of'}),'Origin': soup.find('dd', attrs={'property': 'cidoc:p27_moved_from'}).text,
                       'Support': soup.find('span', attrs={'rel': 'ecidoc:p108i_E12_p126_employed_support'}).text}  # Iterates over list to bring name of the art work.
            df = df.append(new_row, ignore_index=True)  # Appends row to dataframe
        except Exception:
            pass

# Saves dataframe and shows in the screen

df.drop_duplicates()
df.to_csv("art_data", ',')
print(df)
