from urllib.request import *
from bs4 import BeautifulSoup
import pprint

req = Request('https://www.museodelprado.es/en/the-collection/art-works', headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
soup= BeautifulSoup(webpage, 'html.parser')
# Find all <a> in your HTML that have a not null 'href'. Keep only 'href'.
links = [a["href"] for a in soup.find_all("a", href=True)]
links = [x for x in links if x.startswith('https://www.museodelprado.es/en/the-collection/art-work/')]
res = []
[res.append(x) for x in links if x not in res]
pprint.pprint(res)