import urllib.request
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

    for elem in missions:
        position = elem['href'].find("MCode=") + 6

        code_mission = elem['href'][position:]  # Code mission
        name_mission = elem.contents[0]  # Name mission

        image = soup.find_all(alt=name_mission)
        image_mission = image[0]['src'][2:]  # Image mission url

        detail_list = get_detail(target, code_mission)

        print(name_mission + " - " + code_mission + " - " + image_mission + " - " + str(detail_list))


if __name__ == "__main__":
    get_list_missions("Mars")
