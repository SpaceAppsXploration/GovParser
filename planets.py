import json
import random

planets = []
mercury = {}
mercury['name'] = 'Mercury'
mercury['slug'] = 'mercury'
mercury['distance'] = 0.4
mercury['earth_obs'] = False
mercury['cel_body_obs'] = True
mercury['deep_space_obs'] = False
mercury['atm_analysis'] = True
mercury['sample_collect'] = True
mercury['telecom'] = False

planets.append(mercury)

venus = {}
venus['name'] = 'Venus'
venus['slug'] = 'venus'
venus['distance'] = 0.7
venus['earth_obs'] = False
venus['cel_body_obs'] = True
venus['deep_space_obs'] = False
venus['atm_analysis'] = True
venus['sample_collect'] = True
venus['telecom'] = False

planets.append(venus)

earth = {}
earth['name'] = 'Earth'
earth['slug'] = 'earth'
earth['distance'] = 1
earth['earth_obs'] = True
earth['cel_body_obs'] = False
earth['deep_space_obs'] = True
earth['atm_analysis'] = True
earth['sample_collect'] = False
earth['telecom'] = True

planets.append(earth)

moon = {}
moon['name'] = 'Moon'
moon['slug'] = 'moon'
moon['distance'] = 1
moon['earth_obs'] = False
moon['cel_body_obs'] = True
moon['deep_space_obs'] = False
moon['atm_analysis'] = False
moon['sample_collect'] = True
moon['telecom'] = False

planets.append(moon)

mars = {}
mars['name'] = 'Mars'
mars['slug'] = 'mars'
mars['distance'] = 1.5
mars['earth_obs'] = False
mars['cel_body_obs'] = True
mars['deep_space_obs'] = False
mars['atm_analysis'] = True
mars['sample_collect'] = True
mars['telecom'] = False

planets.append(mars)

asteroids = {}
asteroids['name'] = 'Asteroids'
asteroids['slug'] = 'asteroids'
asteroids['distance'] = 2.8
asteroids['earth_obs'] = False
asteroids['cel_body_obs'] = True
asteroids['deep_space_obs'] = False
asteroids['atm_analysis'] = False
asteroids['sample_collect'] = True
asteroids['telecom'] = False

planets.append(asteroids)

jupiter = {}
jupiter['name'] = 'Jupiter'
jupiter['slug'] = 'jupiter'
jupiter['distance'] = 5.2
jupiter['earth_obs'] = False
jupiter['cel_body_obs'] = True
jupiter['deep_space_obs'] = False
jupiter['atm_analysis'] = True
jupiter['sample_collect'] = True
jupiter['telecom'] = False

planets.append(jupiter)

saturn = {}
saturn['name'] = 'Saturn'
saturn['slug'] = 'saturn'
saturn['distance'] = 9.5
saturn['earth_obs'] = False
saturn['cel_body_obs'] = True
saturn['deep_space_obs'] = False
saturn['atm_analysis'] = True
saturn['sample_collect'] = True
saturn['telecom'] = False

planets.append(saturn)

uranus = {}
uranus['name'] = 'Uranus'
uranus['slug'] = 'uranus'
uranus['distance'] = 19.2
uranus['earth_obs'] = False
uranus['cel_body_obs'] = True
uranus['deep_space_obs'] = False
uranus['atm_analysis'] = True
uranus['sample_collect'] = True
uranus['telecom'] = False

planets.append(uranus)

neptune = {}
neptune['name'] = 'Neptune'
neptune['slug'] = 'neptune'
neptune['distance'] = 30
neptune['earth_obs'] = False
neptune['cel_body_obs'] = True
neptune['deep_space_obs'] = False
neptune['atm_analysis'] = True
neptune['sample_collect'] = True
neptune['telecom'] = False

planets.append(neptune)

comets = {}
comets['name'] = 'Comets'
comets['slug'] = 'comets'
comets['distance'] = 10
comets['earth_obs'] = False
comets['cel_body_obs'] = True
comets['deep_space_obs'] = False
comets['atm_analysis'] = False
comets['sample_collect'] = True
comets['telecom'] = False

planets.append(comets)

space = {}
space['name'] = 'Space'
space['slug'] = 'space'
space['distance'] = 50
space['earth_obs'] = False
space['cel_body_obs'] = False
space['deep_space_obs'] = True
space['atm_analysis'] = False
space['sample_collect'] = False
space['telecom'] = False

planets.append(space)





#j = json.dumps(planets)

#myFile = open('planets.json','w')
#myFile.write(j)
#myFile.close()


mission_type = []

earth_obs = {}
earth_obs['name'] = 'Earth observation'
earth_obs['slug'] = 'earth_obs'
earth_obs['opt_sensor'] = True
earth_obs['radio_sensor'] = True
earth_obs['spectr'] = False
earth_obs['probe'] = False
earth_obs['ampli'] = False

mission_type.append(earth_obs)


body_obs = {}
body_obs['name'] = 'Body observation'
body_obs['slug'] = 'cel_body_obs'
body_obs['opt_sensor'] = True
body_obs['radio_sensor'] = True
body_obs['spectr'] = True
body_obs['probe'] = False
body_obs['ampli'] = False

mission_type.append(body_obs)

space_obs = {}
space_obs['name'] = 'Space observation'
space_obs['slug'] = 'deep_space_obs'
space_obs['opt_sensor'] = True
space_obs['radio_sensor'] = True
space_obs['spectr'] = True
space_obs['probe'] = False
space_obs['ampli'] = True

mission_type.append(space_obs)

atm_analysis = {}
atm_analysis['name'] = 'Atmospheric analysis'
atm_analysis['slug'] = 'atm_analysis'
atm_analysis['opt_sensor'] = True
atm_analysis['radio_sensor'] = True
atm_analysis['spectr'] = True
atm_analysis['probe'] = False
atm_analysis['ampli'] = False

mission_type.append(atm_analysis)

sample_collect = {}
sample_collect['name'] = 'Sample collection'
sample_collect['slug'] = 'sample_collect'
sample_collect['opt_sensor'] = True
sample_collect['radio_sensor'] = False
sample_collect['spectr'] = True
sample_collect['probe'] = True
sample_collect['ampli'] = False

mission_type.append(sample_collect)

telecom = {}
telecom['name'] = 'Telecommunication'
telecom['slug'] = 'telecom'
telecom['opt_sensor'] = False
telecom['radio_sensor'] = False
telecom['spectr'] = False
telecom['probe'] = False
telecom['ampli'] = True

mission_type.append(telecom)


#j = json.dumps(mission_type)

#myFile = open('mission_type.json','w')
#myFile.write(j)
#myFile.close()

usr_planet = random.choice(planets)

usr_mission = random.choice(mission_type)
print  usr_planet['name'], usr_mission['name']


if usr_planet[usr_mission['slug']] != True :
    print False, 'Errore in mission type ' + usr_mission['name']
    


components = ['opt_sensor', 'radio_sensor', 'spectr', 'probe', 'ampli']
comp_samples = random.sample(components, random.randint(1, len(components)))

print comp_samples

for e in comp_samples:
    #print e
    for k in mission_type:
        #print k
        if k['name'] == usr_mission['name']:
            if k[e] != True: 
                print False, 'Errore in component ' + e 























