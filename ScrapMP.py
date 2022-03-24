import time
from selenium import webdriver
from bs4 import BeautifulSoup
from urllib.request import *
from bs4 import BeautifulSoup
import pprint
import _ssl

ssl._create_default_https_context = ssl._create_unverified_context

artist_links_list =[]
def artist_links(url = 'https://www.museodelprado.es/en/the-collection'):
    """This function receives an URL and scraps all the links for artists pages
    """
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    soup = BeautifulSoup(webpage, 'html.parser')
    # Find all <a> in your HTML that have a not null 'href'. Keep only 'href'.
    links = [a["href"] for a in soup.find_all("a", href=True)]
    links = [x for x in links if x.startswith('https://www.museodelprado.es/en/the-collection/artist/')]
    global artist_links_list
    [artist_links_list.append(x) for x in links if x not in artist_links_list]

artist_links('https://www.museodelprado.es/en/the-collection')
pprint.pp(artist_links_list)
#
# driver = webdriver.Chrome('/webdrivers/chromedriver.exe')
# driver.get("https://www.museodelprado.es/coleccion/obras-de-arte")
#
# SCROLL_PAUSE_TIME = 20
#
# # Get scroll height
# last_height = driver.execute_script("return document.body.scrollHeight")
#
# while True:
#     # Scroll down to bottom
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#
#     # Wait to load page
#     time.sleep(SCROLL_PAUSE_TIME)
#
#     # Calculate new scroll height and compare with last scroll height
#     new_height = driver.execute_script("return document.body.scrollHeight")
#     if new_height == last_height:
#         break
#     last_height = new_height
#
#  ##### Extract Art URLs #####
#     artist_links_list = []
#     soup = BeautifulSoup(driver.page_source, "html.parser")
#     links = [a["href"] for a in soup.find_all("a", href=True)]
#     links = [x for x in links if x.startswith('https://www.museodelprado.es/en/the-collection/art-work/')]
#     [artist_links_list.append(x) for x in links if x not in artist_links_list]

#
# artist_links_list =[]
# def artist_links(url = 'https://www.museodelprado.es/coleccion/obras-de-arte'):
#     """This function receives an URL and scraps all the links for artists pages
#
#     """
#     ssl._create_default_https_context = ssl._create_unverified_context
#     req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
#     webpage = urlopen(req).read()
#     soup = BeautifulSoup(webpage, 'html.parser')
#     # Find all <a> in your HTML that have a not null 'href'. Keep only 'href'.
#     links = [a["href"] for a in soup.find_all("a", href=True)]
#     links = [x for x in links if x.startswith('https://www.museodelprado.es/coleccion/obra-de-arte/')]
#     global artist_links_list
#     [artist_links_list.append(x) for x in links if x not in artist_links_list]
#
# artist_links('https://www.museodelprado.es/coleccion/obras-de-arte')
# pprint.pp(artist_links_list)