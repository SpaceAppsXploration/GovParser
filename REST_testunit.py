import urllib.request, json
#from bs4 import BeautifulSoup
import random
import re
import time
import json
from pprint import pprint
import datetime




row1 = ('www.spacexplore.it/simulation/?destination=mars&mission=atm_analysis',
        '{"status": "OK", "content": "null", "message": "Mission is way to go!", "code": 0, "type": "cheer"}')
row2 = ('www.spacexplore.it/simulation/?destination=saturn&mission=telecom',
        '{"status": "Error", "content": "Telecom is intended for Earth, thus stay close to Gaia.", "message": "Error in simulation", "code": 1, "type": "Error in mission type telecom"}')
row3 = ('www.spacexplore.it/simulation/?destination=mars&mission=atm_analysis&amplifier=true',
        '{"status": "Error", "content": "Maybe in the BUS", "message": "Error in simulation", "code": 1, "type": "Error in component amplifier"}')

row4 = ('www.spacexplore.it/simulation/?destination=mars&mission=sample_collect&aodcs_simple=bustrue',
        '{"status": "Error", "content": "Does it makes sense to send a BUS with no payload?", "message": "Error in simulation", "code": 1, "type": "Error in payload number check"}')
row5 = ('www.spacexplore.it/simulation/?destination=earth&mission=sample_collect',
        '{"status": "Error", "content": "You do not need a probe to collect samples from Earth. Use a bulldozer instead!", "message": "Error in simulation", "code": 1, "type": "Error in mission type sample_collect"}')
row6 = ('www.spacexplore.it/simulation/?destination=titan&mission=sample_collect&probe=true&opt_sensor=true&therm_active=bustrue&pow_prim_rtg=bustrue&pow_sec_fc=bustrue&comm_mono=bustrue&aodcs_robust=bustrue&prop_electr=bustrue&cdh_optim=bustrue&struct_high_resist=bustrue',
        '{"status": "OK", "content": "null", "message": "Mission is way to go!", "code": 0, "type": "cheer"}')
row7 = ('www.spacexplore.it/simulation/?destination=earth&mission=telecom&amplifier=true&therm_active=bustrue&pow_prim_panels=bustrue&pow_sec_batt=bustrue&comm_omni=bustrue&aodcs_robust=bustrue&prop_chem=bustrue&cdh_optim=bustrue&struct_stand=bustrue',
        '{"status": "OK", "content": "null", "message": "Mission is way to go!", "code": 0, "type": "cheer"}')
row8 = ('www.spacexplore.it/simulation/?destination=asteroids&mission=atm_analysis',
        '{"status": "Error", "content": "Asteroids do not have an atmosphere.", "message": "Error in simulation", "code": 1, "type": "Error in mission type atm_analysis"}')
row9 = ('www.spacexplore.it/simulation/?destination=mercury&mission=sample_collect&amplifier=true',
        '{"status": "Error", "content": "You have to bring the sample back", "message": "Error in simulation", "code": 1, "type": "Error in component amplifier"}')
row10 = ('www.spacexplore.it/simulation/?destination=halley&mission=sample_collect&opt_sensor=true&spectrometer=true',
        '{"status": "OK", "content": "null", "message": "Mission is way to go!", "code": 0, "type": "cheer"}')
row11 = ('www.spacexplore.it/simulation/?destination=halley&mission=sample_collect&opt_sensor=true&amplifier=true',
        '{"status": "Error", "content": "You have to bring the sample back", "message": "Error in simulation", "code": 1, "type": "Error in component amplifier"}')
row12 = ('www.spacexplore.it/simulation/?destination=jupiter&mission=atm_analysis&spectrometer=true&pow_prim_rtg=bustrue',
        '{"status": "OK", "content": "null", "message": "Mission is way to go!", "code": 0, "type": "cheer"}')
row13 = ('www.spacexplore.it/simulation/?destination=titan&mission=atm_analysis&spectrometer=true&prop_electr=bustrue',
        '{"status": "OK", "content": "null", "message": "Mission is way to go!", "code": 0, "type": "cheer"}')


tests = [row1, row2, row3, row4, row5, row6, row7, row8, row9, row9, row10, row11, row12, row13]

for t in tests:
    response = urllib.request.urlopen('http://'+t[0])
    html = json.dumps(response.read().decode('utf-8'))
    #pprint(html)
    #pprint(json.dumps(t[1]))
    m = json.loads(t[1])
    res = json.dumps(t[1])
    if html == res:
        # m = 
        pprint('test passed')
        pprint(m['message'])
    else:
        pprint('not passed')
