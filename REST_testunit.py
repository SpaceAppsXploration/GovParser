'''
TestUnit for local and remote server.
From the command line use parameters:
@ --local for local server
@ --remote for remote server
'''
#import urllib.request, json
#from bs4 import BeautifulSoup
#import random
#import re
import time
import json
from pprint import pprint
#import datetime
import sys
import requests



try:
    arg = sys.argv[1]
    print(sys.argv[1])
    if arg == '--local':
        domain = 'http://localhost:8000'
    elif arg == '--remote':
        domain = 'http://www.spacexplore.it'
except:
    pprint('No Argument Set: set --local or --remote from command line')
    raise SystemExit()

tests = [(domain+'/simulation/?destination=mars&mission=atm_analysis',
        '{"status": "OK", "content": "null", "message": "Mission is way to go!", "code": 0, "type": "cheer"}')
,(domain+'/simulation/?destination=saturn&mission=telecom',
        '{"status": "Error", "content": "Telecom is intended for Earth, thus stay close to Gaia.", "message": "Error in simulation", "code": 1, "type": "Error in mission type telecom"}')
,(domain+'/simulation/?destination=mars&mission=atm_analysis&amplifier=true',
        '{"status": "Error", "content": "Maybe in the BUS", "message": "Error in simulation", "code": 1, "type": "Error in component amplifier"}')

,(domain+'/simulation/?destination=mars&mission=sample_collect&aodcs_simple=bustrue',
        '{"status": "Error", "content": "Does it makes sense to send a BUS with no payload?", "message": "Error in simulation", "code": 1, "type": "Error in payload number check"}')
,(domain+'/simulation/?destination=earth&mission=sample_collect',
        '{"status": "Error", "content": "You do not need a probe to collect samples from Earth. Use a bulldozer instead!", "message": "Error in simulation", "code": 1, "type": "Error in mission type sample_collect"}')
,(domain+'/simulation/?destination=titan&mission=sample_collect&probe=true&opt_sensor=true&therm_active=bustrue&pow_prim_rtg=bustrue&pow_sec_fc=bustrue&comm_mono=bustrue&aodcs_robust=bustrue&prop_electr=bustrue&cdh_optim=bustrue&struct_high_resist=bustrue',
        '{"status": "OK", "content": "null", "message": "Mission is way to go!", "code": 0, "type": "cheer"}')
,(domain+'/simulation/?destination=earth&mission=telecom&amplifier=true&therm_active=bustrue&pow_prim_panels=bustrue&pow_sec_batt=bustrue&comm_omni=bustrue&aodcs_robust=bustrue&prop_chem=bustrue&cdh_optim=bustrue&struct_stand=bustrue',
        '{"status": "OK", "content": "null", "message": "Mission is way to go!", "code": 0, "type": "cheer"}')
,(domain+'/simulation/?destination=asteroids&mission=atm_analysis',
        '{"status": "Error", "content": "Asteroids do not have an atmosphere.", "message": "Error in simulation", "code": 1, "type": "Error in mission type atm_analysis"}')
,(domain+'/simulation/?destination=mercury&mission=sample_collect&amplifier=true',
        '{"status": "Error", "content": "You have to bring the sample back", "message": "Error in simulation", "code": 1, "type": "Error in component amplifier"}')
,(domain+'/simulation/?destination=halley&mission=sample_collect&opt_sensor=true&spectrometer=true',
        '{"status": "OK", "content": "null", "message": "Mission is way to go!", "code": 0, "type": "cheer"}')
,(domain+'/simulation/?destination=halley&mission=sample_collect&opt_sensor=true&amplifier=true',
        '{"status": "Error", "content": "You have to bring the sample back", "message": "Error in simulation", "code": 1, "type": "Error in component amplifier"}')
,(domain+'/simulation/?destination=jupiter&mission=atm_analysis&spectrometer=true&pow_prim_rtg=bustrue',
        '{"status": "OK", "content": "null", "message": "Mission is way to go!", "code": 0, "type": "cheer"}')
,(domain+'/simulation/?destination=titan&mission=atm_analysis&spectrometer=true&prop_electr=bustrue',
        '{"status": "OK", "content": "null", "message": "Mission is way to go!", "code": 0, "type": "cheer"}')
]

pprint('---------------------------')
count = 0
for t in tests:
    # response = urllib.request.urlopen(t[0]) using urllib replying binary
    r = requests.get(t[0])
    #html = json.dumps(response.read().decode('utf-8'))
    #pprint(response.text)
    #pprint(t[1])
    #pprint(json.dumps(t[1]))
    pprint('Time delta: '+ str(r.elapsed))
    m = json.loads(t[1])
    r = r.json()
    #res = json.dumps(t[1])
    #if html == res:
    if r == m:
        pprint('TEST: '+ str(count))
        pprint('test passed')
        pprint(m['message'])
        pprint('---------------------------')
    else:
        pprint('not passed')
        break
    count += 1
