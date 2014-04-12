import urllib.request, json
from bs4 import BeautifulSoup

url = 'http://solarsystem.nasa.gov/missions/profile.cfm?'


def get_detail(target, code):
    response = urllib.request.urlopen(str(url + "Target=" + target + "&MCode=" + code))
    html_doc = response.read()

    soup = BeautifulSoup(html_doc)

    details = soup.find_all("p")

    details_list = []
    for detail in details:
        if details.index(detail) != 2:
            if len(detail.contents) > 1:
                details_list.append(detail.contents[1][2:])
        else:
            details_list.append(detail.contents[0])

    extra_details = soup.find_all("div", class_="l2eventdateblack")

    for extra_detail in extra_details:
        if extra_detail.contents[1].name != "a" and len(extra_detail.contents[2].strip(u'\xa0')) != 0:
            details_list.append({extra_detail.contents[1].contents[0]: extra_detail.contents[2].strip(u'\xa0')})

    links = soup.find_all("a", class_="l2missionfeaturelink")

    link = links[1]['href']

    details_list.append(link)

    return details_list


def get_list_missions(target):
    # get page
    response = urllib.request.urlopen(str(url + "Target=" + target))
    html_doc = response.read()

    soup = BeautifulSoup(html_doc)

    # find all hyperlinks
    missions = soup.find_all("a", class_="l2missiontitle")

    missions_list = []
    for i in range(0, 4):
        position = missions[i]['href'].find("MCode=") + 6

        code_mission = (missions[i])['href'][position:]  # Code mission
        name_mission = (missions[i]).contents[0]  # Name mission

        image = soup.find_all(alt=name_mission)
        image_mission = image[0]['src'][2:]  # Image mission url

        detail_list = get_detail(target, code_mission)

        # print(detail_list)
        # key_date = []
        # for alfa in detail_list[3]:
        #     key_date.append('" ' + alfa[0] + '" : "' + alfa[1] + '",')

        #mission = '{"code" : ' + name_mission + ', "hashed" : ' + code_mission + ', "image_url : "' + image_mission + ', "goals" : ' + detail_list[0] + ', "accomplished" : ' + detail_list[1] + ', "link" : ' + detail_list[-1] + ', "headlines" : /news/archive.cfm?Mission=' + code_mission + ', "mission_type" : null , "destination" : ' + target + ', "key_date" : ' + str(key_date) + '}'

        #print(detail_list[3])
        mission = {}
        mission["hashed"] = code_mission
        mission["code"] = name_mission
        mission["goals"] = detail_list[0]
        accomplish = detail_list[1]
        mission["accomplished"] = accomplish
        mission["link"] = detail_list[-1]
        #mission["key_dates"] = detail_list[3][0]
        mission["headlines"] = '/news/archive.cfm?Mission=' + code_mission
        mission["mission_type"] = 'null'
        mission["image_url"] = image_mission
        mission["destination"] = target

        missions_list.append(mission)

    js = json.dumps(missions_list)
    print(js)

if __name__ == "__main__":
    get_list_missions("Mars")

    #Mercury Venus Moon Mars Asteroids Dwarf Planets Jupiter Saturn Uranus Neptune Kuiper Belt Beyond
