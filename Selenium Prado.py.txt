# Import Libraries
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import csv
import re
import json

s = Service('./chromedriver.exe')
browser = webdriver.Chrome(service=s)

browser.get('https://www.museodelprado.es/coleccion/obras-de-arte')

scroll = browser.find_element(by=By.TAG_NAME, value="body")

no_of_pagedowns = 2000
while no_of_pagedowns:  # Loops using page downs to scroll all the page and load all html code
    scroll.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.2)
    no_of_pagedowns-=1

#for i in range(1500): # adjust integer value for need
#       # you can change right side number for scroll convenience or destination
#       browser.execute_script("window.scrollBy(0, 1500)")
#       # you can change time integer to float or remove
#       time.sleep(0.5)

# Obtener los links de las obras
links = browser.find_elements(by=By.XPATH, value="//div[@class='imgwrap']//a")
list_links = []

for x in links:
    list_links.append(x.get_attribute("href"))
print(len(list_links))

# Nos quedamos solo con aquellos links válidos (los que contienen en la URL /obra-de-arte/)
r = re.compile(".*obra-de-arte")
pattern = r'[]'
list_links = list(filter(r.match, list_links))
print(len(list_links))

# Obtener las imágenes de los cuadros (en formato .jpg)
imagenes = browser.find_elements(by=By.XPATH, value="//div[@class='imgwrap']//img")
list_jpgs = []

for y in imagenes:
    list_jpgs.append(y.get_attribute("src"))
print(len(list_jpgs))


# Escribimos los links en un archivo links.txt
with open('links.txt', 'w') as f:  # Save in txt file
    f.write(json.dumps(list_links))

# Escribimos los enlaces de las imágenes en un archivo jpgs.txt
with open('jpgs.txt', 'w') as f:  # Save in txt file
    f.write(json.dumps(list_jpgs))