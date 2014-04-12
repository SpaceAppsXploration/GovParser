import urllib.request
from bs4 import BeautifulSoup

def is_link(tag):
	if tag.name == 'a':
	    print(tag)

# define URL

url = 'http://solarsystem.nasa.gov/missions/profile.cfm?'

target = 'Target=Mars'

# get page

reponse = urllib.request.urlopen(str(url+target))

htmlDoc = reponse.read()

soup = BeautifulSoup(htmlDoc)

# find all hyperlinks

parent = soup.find_all("div", class_="l2text")

parent = BeautifulSoup(''.join(parent))

hyperlinks = parent.find_all(is_link)

# get links inside div class l2text

#print(hyperlinks)
