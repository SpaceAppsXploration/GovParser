import urllib.request
from bs4 import BeautifulSoup

# define URL

url = 'http://solarsystem.nasa.gov/missions/profile.cfm?'

target = 'Target=Mars'

# get page

reponse = urllib.request.urlopen(str(url+target))

htmlDoc = reponse.read()

soup = BeautifulSoup(htmlDoc)

# find all hyperlinks

parent = soup.find_all("a", class_="l2missiontitle")


for elem in parent:
    position = elem['href'].find("MCode=") + 6
    print(elem['href'][position:]) #Code mission
    print(elem.contents) #Name mission

