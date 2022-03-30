# Import Libraries
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pprint
import csv
import json

browser = webdriver.Chrome("C:/webdrivers/chromedriver.exe")

browser.get('https://www.museodelprado.es/coleccion/obras-de-arte?ordenarPor=ecidoc:p62_E52_p79_has_time-span_beginning&pm:departmentName=Pintura%20barroca%20espa%C3%B1ola&pm:departmentName=Pintura%20espa%C3%B1ola%20del%20renacimiento%20y%20primer%20naturalismo&pm:departmentName=Pintura%20espa%C3%B1ola%20hasta%201500&pm:departmentName=Pintura%20espa%C3%B1ola%20siglo%20XVIII&pm:departmentName=Pintura%20espa%C3%B1ola%20hasta%201800&orden=asc')
time.sleep(1)

elem = browser.find_element_by_tag_name("body")

no_of_pagedowns = 150
while no_of_pagedowns:  # Loops using page downs to scroll all the page and load all html code
    elem.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.2)
    no_of_pagedowns-=1

post_elems = browser.find_elements_by_tag_name("a")
list_links = []
for post in post_elems:  # Append links in the page to this list
    list_links.append(post.get_attribute('href'))
print(len(list_links))

list_links = [i for i in list_links if i]  # Remove None values
print(len(list_links))

list_links = [x for x in list_links if x.startswith('https://www.museodelprado.es/coleccion/obra-de-arte/')]  # Get only art work links
print(len(list_links))

res = []
[res.append(x) for x in list_links if x not in res]  # Remove Duplicates
print(len(res))
pprint.pp(res)


with open('test.txt', 'w') as f:  # Save in txt file
    f.write(json.dumps(res))

