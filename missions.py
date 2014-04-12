import urllib.request
from bs4 import BeautifulSoup

url = 'http://solarsystem.nasa.gov/missions/profile.cfm?'

target = 'Target=Mars'

reponse = urllib.request.urlopen(str(url+target))

htmlDoc = reponse.read()

soup = BeautifulSoup(htmlDoc)

hyperlinks = soup.find_all('a')

print(hyperlinks)
