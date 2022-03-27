import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pprint

browser = webdriver.Chrome("C:/webdrivers/chromedriver.exe")

browser.get('https://www.museodelprado.es/coleccion/obras-de-arte')
time.sleep(1)

elem = browser.find_element_by_tag_name("body")

no_of_pagedowns = 45
while no_of_pagedowns:
    elem.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.2)
    no_of_pagedowns-=1

post_elems = browser.find_elements_by_tag_name("a")
list_links = []
for post in post_elems:
    list_links.append(post.get_attribute('href'))
print(len(list_links))

list_links = [i for i in list_links if i]
print(len(list_links))

list_links= [x for x in list_links if x.startswith('https://www.museodelprado.es/coleccion/obra-de-arte/')]
print(len(list_links))

res = []
[res.append(x) for x in list_links if x not in res]
print(len(res))