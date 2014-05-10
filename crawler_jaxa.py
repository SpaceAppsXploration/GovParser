import requests
from bs4 import BeautifulSoup
import random
import re
import time
import json
from pprint import pprint

from JAXA_missions_list import  missions

def get_detailed_page(missions, RESULTS):
        i = 1
        planets = ["Earth", "Venus", "Mercury", "Mars", "Saturn", "Jupiter", "Neptune", "Uranus", "Solar", "Moon"]

        for m in missions:
          if "sat" in m["link"][0]:
                  result = {}
                  link = m["link"][0]
                  result["era"] = 2
                  result["target"] = 1
                  #print("\n\n")
                  #print(link)
                  tmp = m["name"][0]
                  if len(link.split("/")) > 6:
                          name = link.split("/")[5]
                  for elem in planets:
                    if elem in tmp:
                      result["target"] = elem           #TARGET
                  result["name"] = tmp                  #NAME
                  result["link"] = link                 #LINK
                  result["hashed"] = name
                  result["codename"] = name
                  #HASHED
                  response = requests.get(link)
                  soup = BeautifulSoup(str(response.text))
                  head = soup.find(class_="elem_heading_lv2_pad")
                  parent = str(head.find_next("img"))
                  index = parent.find("src")            #find the beginning of the mission's image
                  end = parent.find(".jpg")             #find the end of the mission's image
                  img = parent[index+5:end+4]
                  if (img[:4] == "imag"):
                          prov = link.split("/")
                          proj = "/"+prov[3]+"/"+prov[4]+"/"+prov[5]+"/"
                          img = proj+img
                  if (img[:4] != "http"):
                          img = "http://global.jaxa.jp" + img
                  if soup.find(class_="elem_table_set middle"):
                          launch = soup.find(class_="elem_table_set middle")
                          tab = launch.find_next(class_="elem_table_set middle")
                          if tab:
                                  if (len(tab.contents) == 1):
                                          data = tab.contents[0].split(",")
                                          if len(data) == 2:
                                                  data = data[0] + data[1]
                                          elif len(data) > 2:
                                                  data = data[1][1:] + data[2][:-5]
                          result["date"] = data         #LAUNCH DATA        
                  result["img"] = img                   #IMAGE
                  key = "About " + tmp[:4]
                  test = soup.find_all(text=re.compile(key))
                  #print(test, link, i)
                  i += 1
                  fake = soup.find(class_="elem_pic_block left_pad")
                  real = fake.find_next(class_="elem_pic_block left_pad")
                  parag = real.find(class_="elem_paragraph")
                  text = parag.find_all("p")
                  comp = ""
                  for elem in text:
                          for text in elem.contents:
                                  comp = comp + str(text)
                          
                  #print(comp.replace(".T", ". T"))
                  
          result["jaxa"] = True                         #JAXA
          
          #pprint(result)
          
          RESULTS.append(result)

        pprint(RESULTS)
        return json.dumps(RESULTS)
'''          

        #print(soup)

        RESULTS['name'] = m['name']
        #RESULTS['mission_id'] = id missione dal db
        DATA = [] # array con tutti i dettagli missione da inserire in RESULTS alla fine
        print('NAME: '+m['name'])
        print(str(i))

        #print('GOALS:-----------------------------------------')
        try:
            get_Goals = soup.find_all(text="Goals")
            goals = get_Goals[0].parent.parent
            #print(str(goals.contents[1])[2:])
            DATA.append({'type': 1, 'header': 'Goal', 'body': str(goals.contents[1])[2:]})
        except:
            pass
            

        #print('ACCOMPLISHMENTS:-----------------------------------------')
        try:
            get_Accomplish = soup.find_all(text="Accomplishments")
            accomplish = get_Accomplish[0].parent.parent
            #print(str(accomplish.contents[1])[2:])
            DATA.append({'type': 2, 'header': 'Accomplishment', 'body': str(accomplish.contents[1])[2:]})
        except:
            pass
            

        #print('READ MORE AND MISSION LINK--------------------------')
        links = soup.find_all(class_="l2missionfeaturelink")
        #for e in links:
            # link ai read more o al sito della missione
            # sostituire a ../ l'url nasa.gov
        if len(links) == 2:
                href0 = links[0].get('href')
                href0 = href0.replace('..', 'http://solarsystem.nasa.gov')
                href1 = links[1].get('href')
                href1 = href1.replace('..', 'http://solarsystem.nasa.gov')
                DATA.append({'type': 3, 'header': 'Read More about '+m['name'], 'body': href0})
                DATA.append({'type': 4, 'header': m['name']+' Website', 'body': href1})
                #print(DATA)
        if len(links) == 1:
                href0 = links[0].get('href')
                href0 = href0.replace('..', 'http://solarsystem.nasa.gov')
                DATA.append({'type': 3, 'header': 'Read More about '+m['name'], 'body': href0})
                


        #print('DATES AND HEADLINES ---------------------------------')
        get_Key_Dates = soup.find_all(class_="l2eventdateblack")
        #get_Key_Dates = get_Key_Dates.find_all(class_="l2eventdateblack")
        #get_Key_Dates = get_Key_Dates[1]
        #print(get_Key_Dates[1].contents)
        events = []
        for i in get_Key_Dates:
            contents = []
            for k in range(0, len(i)):
                if i.contents[k].string != '\n':
                    contents.append(str(i.contents[k].string))
            events.append(contents)
            del contents

        #print(events)
        for i,e in enumerate(events):
            if len(e) == 1 and e != 'None' and e[0] != 'None':
                #print(e, i, events[i])
                name = str(events[i][0]).strip()
                if len(events[i-1]) != 1:
                    date = events[i-1][0]
                    date = date[:-1]
                else:
                     date = events[i-1]
                     date = date[:-1]
                #print(name, date)
                if len(date) == 0:
                     date = '1 Jan 1970' # concept mission events have dummy date
                to_push = [date, name]
                events.append(to_push)
                #print(name, date)
                del events[i]
                del events[i-1]
                DATA.append({'type': 5, 'header': 'Event '+date, 'body': name, 'date': date })
            if e[0] == 'Status':
                # save mission status
                DATA.append({'type': 7, 'header': 'Status', 'body': e[1]})

        for i,e in enumerate(events):
            if isinstance(e, list):
                for k,j in enumerate(e):
                   events[i][k] = events[i][k].replace(u'\xa0', u' ').strip()
            else:
                events[i] = events[i].replace(u'\xa0',u' ').strip()
        
        

        #print(str('FAST FACTS AND IMAGE-----------------------------------')) 

        if soup.find_all(src=re.compile("-facts.jpg")):
            get_Features = soup.find_all(src=re.compile("-facts.jpg"))
            #get_Features = soup.find_all(class_="l2featuretext")
            g = get_Features[0]
            #print(str(g.contents[0]).strip())
            #print(g.get('src'))
            href = g.get('src')
            href = href.replace('..', 'http://solarsystem.nasa.gov')
            DATA.append({'type': 6, 'header': 'Fact', 'body': str(g.contents[0]).strip(), 'image_link': href  })


        print(DATA)

        RESULTS['data'] = DATA
        
        TOTALS.append(RESULTS)
        i = i + 1

    TOTALS = json.dumps(TOTALS)
    return TOTALS
        
    '''
        
if __name__ == "__main__":
    TOTALS = []
    TOTALS = get_detailed_page(missions, TOTALS)
    text_file = open("JAXA_output.json", "w")
    text_file.write(TOTALS)
    text_file.close()


