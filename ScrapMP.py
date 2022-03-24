from urllib.request import *
from bs4 import BeautifulSoup
import pprint


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