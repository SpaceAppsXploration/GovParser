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
    


components = ['opt_sensor', 'radio_sensor', 'spectrometer', 'probe', 'amplifier']
comp_samples = random.sample(components, random.randint(1, len(components)))

print comp_samples

for e in comp_samples:
    #print e
    for k in mission_type:
        #print k
        if k['name'] == usr_mission['name']:
            if k[e] != True: 
                print False, 'Errore in component ' + e 


#############################


bus_vs_mission_type = []

earth_obs = {}
earth_obs['name'] = 'Earth observation'
earth_obs['slug'] = 'earth-obs'
earth_obs['therm_active'] = True
earth_obs['therm_passive'] = True
earth_obs['pow_prim_panels'] = True
earth_obs['pow_prim_rtg'] = True
earth_obs['pow_sec_batt'] = True
earth_obs['pow_sec_fc'] = True
earth_obs['comm_mono'] = True
earth_obs['comm_omni'] = True
earth_obs['aodcs_robust'] = True
earth_obs['aodcs_simple'] = True
earth_obs['prop_electr'] = True
earth_obs['prop_chem'] = True
earth_obs['c&dh_standard'] = True
earth_obs['c&dh_optim'] = True
earth_obs['struct_stand'] = True
earth_obs['struct_high_resist'] = True

bus_vs_mission_type.append(earth_obs)


body_obs = {}
body_obs['name'] = 'Body observation'
body_obs['slug'] = 'body-obs'
body_obs['therm_active'] = True
body_obs['therm_passive'] = True
body_obs['pow_prim_panels'] = True
body_obs['pow_prim_rtg'] = True
body_obs['pow_sec_batt'] = True
body_obs['pow_sec_fc'] = True
body_obs['comm_mono'] = True
body_obs['comm_omni'] = True
body_obs['aodcs_robust'] = True
body_obs['aodcs_simple'] = True
body_obs['prop_electr'] = True
body_obs['prop_chem'] = True
body_obs['c&dh_standard'] = True
body_obs['c&dh_optim'] = True
body_obs['struct_stand'] = True
body_obs['struct_high_resist'] = True

bus_vs_mission_type.append(body_obs)



space_obs = {}
space_obs['name'] = 'Space observation'
space_obs['slug'] = 'space-obs'
space_obs['therm_active'] = True
space_obs['therm_passive'] = True
space_obs['pow_prim_panels'] = True
space_obs['pow_prim_rtg'] = True
space_obs['pow_sec_batt'] = True
space_obs['pow_sec_fc'] = True
space_obs['comm_mono'] = True
space_obs['comm_omni'] = True
space_obs['aodcs_robust'] = True
space_obs['aodcs_simple'] = True
space_obs['prop_electr'] = True
space_obs['prop_chem'] = True
space_obs['c&dh_standard'] = True
space_obs['c&dh_optim'] = True
space_obs['struct_stand'] = True
space_obs['struct_high_resist'] = True

bus_vs_mission_type.append(space_obs)



atm_analysis = {}
atm_analysis['name'] = 'Athmosphere Analysis'
atm_analysis['slug'] = 'atm-analysis'
atm_analysis['therm_active'] = True
atm_analysis['therm_passive'] = True
atm_analysis['pow_prim_panels'] = True
atm_analysis['pow_prim_rtg'] = True
atm_analysis['pow_sec_batt'] = True
atm_analysis['pow_sec_fc'] = True
atm_analysis['comm_mono'] = True
atm_analysis['comm_omni'] = True
atm_analysis['aodcs_robust'] = True
atm_analysis['aodcs_simple'] = True
atm_analysis['prop_electr'] = True
atm_analysis['prop_chem'] = True
atm_analysis['c&dh_standard'] = True
atm_analysis['c&dh_optim'] = True
atm_analysis['struct_stand'] = True
atm_analysis['struct_high_resist'] = True

bus_vs_mission_type.append(atm_analysis)



sample_collect = {}
sample_collect['name'] = 'Samples Collection'
sample_collect['slug'] = 'sample-collect'
sample_collect['therm_active'] = True
sample_collect['therm_passive'] = True
sample_collect['pow_prim_panels'] = True
sample_collect['pow_prim_rtg'] = True
sample_collect['pow_sec_batt'] = True
sample_collect['pow_sec_fc'] = True
sample_collect['comm_mono'] = True
sample_collect['comm_omni'] = True
sample_collect['aodcs_robust'] = True
sample_collect['aodcs_simple'] = False
sample_collect['prop_electr'] = True
sample_collect['prop_chem'] = True
sample_collect['c&dh_standard'] = True
sample_collect['c&dh_optim'] = True
sample_collect['struct_stand'] = True
sample_collect['struct_high_resist'] = True

bus_vs_mission_type.append(sample_collect)



telecom = {}
telecom['name'] = 'Telecommunications'
telecom['slug'] = 'telecom'
telecom['therm_active'] = True
telecom['therm_passive'] = True
telecom['pow_prim_panels'] = True
telecom['pow_prim_rtg'] = True
telecom['pow_sec_batt'] = True
telecom['pow_sec_fc'] = True
telecom['comm_mono'] = True
telecom['comm_omni'] = True
telecom['aodcs_robust'] = True
telecom['aodcs_simple'] = False
telecom['prop_electr'] = True
telecom['prop_chem'] = True
telecom['c&dh_standard'] = False
telecom['c&dh_optim'] = True
telecom['struct_stand'] = True
telecom['struct_high_resist'] = True

bus_vs_mission_type.append(telecom)



######################



bus_vs_PL_type = []

opt_sensor = {}
opt_sensor['name'] = 'Optic Sensor'
opt_sensor['slug'] = 'opt-sensor'
opt_sensor['therm_active'] = True
opt_sensor['therm_passive'] = True
opt_sensor['pow_prim_panels'] = True
opt_sensor['pow_prim_rtg'] = True
opt_sensor['pow_sec_batt'] = True
opt_sensor['pow_sec_fc'] = True
opt_sensor['comm_mono'] = True
opt_sensor['comm_omni'] = True
opt_sensor['aodcs_robust'] = True
opt_sensor['aodcs_simple'] = False
opt_sensor['prop_electr'] = True
opt_sensor['prop_chem'] = True
opt_sensor['c&dh_standard'] = False
opt_sensor['c&dh_optim'] = True
opt_sensor['struct_stand'] = True
opt_sensor['struct_high_resist'] = True

bus_vs_PL_type.append(opt_sensor)



radio_sensor = {}
radio_sensor['name'] = 'Radio Sensor'
radio_sensor['slug'] = 'radio-sensor'
radio_sensor['therm_active'] = True
radio_sensor['therm_passive'] = True
radio_sensor['pow_prim_panels'] = True
radio_sensor['pow_prim_rtg'] = False
radio_sensor['pow_sec_batt'] = True
radio_sensor['pow_sec_fc'] = True
radio_sensor['comm_mono'] = True
radio_sensor['comm_omni'] = True
radio_sensor['aodcs_robust'] = True
radio_sensor['aodcs_simple'] = True
radio_sensor['prop_electr'] = True
radio_sensor['prop_chem'] = True
radio_sensor['c&dh_standard'] = True
radio_sensor['c&dh_optim'] = True
radio_sensor['struct_stand'] = True
radio_sensor['struct_high_resist'] = True

bus_vs_PL_type.append(radio_sensor)



spectr = {}
spectr['name'] = 'Spectrometer'
spectr['slug'] = 'spectr'
spectr['therm_active'] = True
spectr['therm_passive'] = False
spectr['pow_prim_panels'] = True
spectr['pow_prim_rtg'] = False
spectr['pow_sec_batt'] = True
spectr['pow_sec_fc'] = True
spectr['comm_mono'] = True
spectr['comm_omni'] = True
spectr['aodcs_robust'] = True
spectr['aodcs_simple'] = True
spectr['prop_electr'] = False
spectr['prop_chem'] = True
spectr['c&dh_standard'] = True
spectr['c&dh_optim'] = True
spectr['struct_stand'] = True
spectr['struct_high_resist'] = True

bus_vs_PL_type.append(spectr)



probe = {}
probe['name'] = 'Probe'
probe['slug'] = 'probe'
probe['therm_active'] = True
probe['therm_passive'] = True
probe['pow_prim_panels'] = True
probe['pow_prim_rtg'] = True
probe['pow_sec_batt'] = True
probe['pow_sec_fc'] = True
probe['comm_mono'] = True
probe['comm_omni'] = True
probe['aodcs_robust'] = True
probe['aodcs_simple'] = False
probe['prop_electr'] = True
probe['prop_chem'] = True
probe['c&dh_standard'] = True
probe['c&dh_optim'] = True
probe['struct_stand'] = False
probe['struct_high_resist'] = True

bus_vs_PL_type.append(probe)



ampli = {}
ampli['name'] = 'Amplifier'
ampli['slug'] = 'ampli'
ampli['therm_active'] = True
ampli['therm_passive'] = True
ampli['pow_prim_panels'] = True
ampli['pow_prim_rtg'] = True
ampli['pow_sec_batt'] = True
ampli['pow_sec_fc'] = True
ampli['comm_mono'] = True
ampli['comm_omni'] = True
ampli['aodcs_robust'] = True
ampli['aodcs_simple'] = True
ampli['prop_electr'] = True
ampli['prop_chem'] = True
ampli['c&dh_standard'] = True
ampli['c&dh_optim'] = True
ampli['struct_stand'] = True
ampli['struct_high_resist'] = True

bus_vs_PL_type.append(ampli)



###################################



bus_vs_bus = []

therm_active = {}
therm_active['name'] = 'Thermal Active'
therm_active['slug'] = 'therm-active'
therm_active['therm_active'] = True
therm_active['therm_passive'] = False
therm_active['pow_prim_panels'] = True
therm_active['pow_prim_rtg'] = True
therm_active['pow_sec_batt'] = True
therm_active['pow_sec_fc'] = True
therm_active['comm_mono'] = True
therm_active['comm_omni'] = True
therm_active['aodcs_robust'] = False
therm_active['aodcs_simple'] = True
therm_active['prop_electr'] = True
therm_active['prop_chem'] = True
therm_active['c&dh_standard'] = True
therm_active['c&dh_optim'] = True
therm_active['struct_stand'] = True
therm_active['struct_high_resist'] = True

bus_vs_bus.append(therm_active)



therm_passive = {}
therm_passive['name'] = 'Thermal Passive'
therm_passive['slug'] = 'therm-passive'
therm_passive['therm_active'] = False
therm_passive['therm_passive'] = True
therm_passive['pow_prim_panels'] = True
therm_passive['pow_prim_rtg'] = True
therm_passive['pow_sec_batt'] = True
therm_passive['pow_sec_fc'] = True
therm_passive['comm_mono'] = True
therm_passive['comm_omni'] = True
therm_passive['aodcs_robust'] = True
therm_passive['aodcs_simple'] = False
therm_passive['prop_electr'] = True
therm_passive['prop_chem'] = True
therm_passive['c&dh_standard'] = True
therm_passive['c&dh_optim'] = True
therm_passive['struct_stand'] = True
therm_passive['struct_high_resist'] = True

bus_vs_bus.append(therm_passive)



pow_prim_panels = {}
pow_prim_panels['name'] = 'Primary Power Solar Arrays'
pow_prim_panels['slug'] = 'pow-prim-panels'
pow_prim_panels['therm_active'] = True
pow_prim_panels['therm_passive'] = True
pow_prim_panels['pow_prim_panels'] = True
pow_prim_panels['pow_prim_rtg'] = False
pow_prim_panels['pow_sec_batt'] = True
pow_prim_panels['pow_sec_fc'] = True
pow_prim_panels['comm_mono'] = True
pow_prim_panels['comm_omni'] = True
pow_prim_panels['aodcs_robust'] = True
pow_prim_panels['aodcs_simple'] = False
pow_prim_panels['prop_electr'] = True
pow_prim_panels['prop_chem'] = True
pow_prim_panels['c&dh_standard'] = True
pow_prim_panels['c&dh_optim'] = True
pow_prim_panels['struct_stand'] = True
pow_prim_panels['struct_high_resist'] = True

bus_vs_bus.append(pow_prim_panels)



pow_prim_rtg = {}
pow_prim_rtg['name'] = 'Primary Power RTG'
pow_prim_rtg['slug'] = 'pow-prim-rtg'
pow_prim_rtg['therm_active'] = True
pow_prim_rtg['therm_passive'] = True
pow_prim_rtg['pow_prim_panels'] = False
pow_prim_rtg['pow_prim_rtg'] = True
pow_prim_rtg['pow_sec_batt'] = True
pow_prim_rtg['pow_sec_fc'] = False
pow_prim_rtg['comm_mono'] = True
pow_prim_rtg['comm_omni'] = True
pow_prim_rtg['aodcs_robust'] = True
pow_prim_rtg['aodcs_simple'] = True
pow_prim_rtg['prop_electr'] = True
pow_prim_rtg['prop_chem'] = True
pow_prim_rtg['c&dh_standard'] = True
pow_prim_rtg['c&dh_optim'] = True
pow_prim_rtg['struct_stand'] = False
pow_prim_rtg['struct_high_resist'] = True

bus_vs_bus.append(pow_prim_rtg)



pow_sec_batt = {}
pow_sec_batt['name'] = 'Backup Power Batteries'
pow_sec_batt['slug'] = 'pow-sec-batt'
pow_sec_batt['therm_active'] = True
pow_sec_batt['therm_passive'] = True
pow_sec_batt['pow_prim_panels'] = True
pow_sec_batt['pow_prim_rtg'] = True
pow_sec_batt['pow_sec_batt'] = True
pow_sec_batt['pow_sec_fc'] = True
pow_sec_batt['comm_mono'] = True
pow_sec_batt['comm_omni'] = True
pow_sec_batt['aodcs_robust'] = True
pow_sec_batt['aodcs_simple'] = True
pow_sec_batt['prop_electr'] = True
pow_sec_batt['prop_chem'] = True
pow_sec_batt['c&dh_standard'] = True
pow_sec_batt['c&dh_optim'] = True
pow_sec_batt['struct_stand'] = True
pow_sec_batt['struct_high_resist'] = True

bus_vs_bus.append(pow_sec_batt)



pow_sec_fc = {}
pow_sec_fc['name'] = 'Backup Power Fuel Cells'
pow_sec_fc['slug'] = 'pow-sec-fc'
pow_sec_fc['therm_active'] = True
pow_sec_fc['therm_passive'] = True
pow_sec_fc['pow_prim_panels'] = True
pow_sec_fc['pow_prim_rtg'] = False
pow_sec_fc['pow_sec_batt'] = True
pow_sec_fc['pow_sec_fc'] = True
pow_sec_fc['comm_mono'] = True
pow_sec_fc['comm_omni'] = True
pow_sec_fc['aodcs_robust'] = True
pow_sec_fc['aodcs_simple'] = True
pow_sec_fc['prop_electr'] = False
pow_sec_fc['prop_chem'] = True
pow_sec_fc['c&dh_standard'] = True
pow_sec_fc['c&dh_optim'] = True
pow_sec_fc['struct_stand'] = True
pow_sec_fc['struct_high_resist'] = True

bus_vs_bus.append(pow_sec_fc)



comm_mono = {}
comm_mono['name'] = 'Communication Monodirectional'
comm_mono['slug'] = 'comm-mono'
comm_mono['therm_active'] = True
comm_mono['therm_passive'] = True
comm_mono['pow_prim_panels'] = True
comm_mono['pow_prim_rtg'] = True
comm_mono['pow_sec_batt'] = True
comm_mono['pow_sec_fc'] = True
comm_mono['comm_mono'] = True
comm_mono['comm_omni'] = False
comm_mono['aodcs_robust'] = True
comm_mono['aodcs_simple'] = False
comm_mono['prop_electr'] = True
comm_mono['prop_chem'] = True
comm_mono['c&dh_standard'] = True
comm_mono['c&dh_optim'] = True
comm_mono['struct_stand'] = True
comm_mono['struct_high_resist'] = True

bus_vs_bus.append(comm_mono)



comm_omni = {}
comm_omni['name'] = 'Communication Omnidirectional'
comm_omni['slug'] = 'comm-omni'
comm_omni['therm_active'] = True
comm_omni['therm_passive'] = True
comm_omni['pow_prim_panels'] = True
comm_omni['pow_prim_rtg'] = True
comm_omni['pow_sec_batt'] = True
comm_omni['pow_sec_fc'] = True
comm_omni['comm_mono'] = False
comm_omni['comm_omni'] = True
comm_omni['aodcs_robust'] = True
comm_omni['aodcs_simple'] = True
comm_omni['prop_electr'] = True
comm_omni['prop_chem'] = True
comm_omni['c&dh_standard'] = False
comm_omni['c&dh_optim'] = True
comm_omni['struct_stand'] = True
comm_omni['struct_high_resist'] = True

bus_vs_bus.append(comm_omni)



aodcs_robust = {}
aodcs_robust['name'] = 'AODCS Robust'
aodcs_robust['slug'] = 'aodcs-robust'
aodcs_robust['therm_active'] = False
aodcs_robust['therm_passive'] = True
aodcs_robust['pow_prim_panels'] = True
aodcs_robust['pow_prim_rtg'] = True
aodcs_robust['pow_sec_batt'] = True
aodcs_robust['pow_sec_fc'] = True
aodcs_robust['comm_mono'] = True
aodcs_robust['comm_omni'] = True
aodcs_robust['aodcs_robust'] = True
aodcs_robust['aodcs_simple'] = False
aodcs_robust['prop_electr'] = True
aodcs_robust['prop_chem'] = True
aodcs_robust['c&dh_standard'] = True
aodcs_robust['c&dh_optim'] = True
aodcs_robust['struct_stand'] = True
aodcs_robust['struct_high_resist'] = True

bus_vs_bus.append(aodcs_robust)



aodcs_simple = {}
aodcs_simple['name'] = 'AODCS Simple'
aodcs_simple['slug'] = 'aodcs-simple'
aodcs_simple['therm_active'] = True
aodcs_simple['therm_passive'] = False
aodcs_simple['pow_prim_panels'] = False
aodcs_simple['pow_prim_rtg'] = True
aodcs_simple['pow_sec_batt'] = True
aodcs_simple['pow_sec_fc'] = True
aodcs_simple['comm_mono'] = False
aodcs_simple['comm_omni'] = True
aodcs_simple['aodcs_robust'] = False
aodcs_simple['aodcs_simple'] = True
aodcs_simple['prop_electr'] = True
aodcs_simple['prop_chem'] = False
aodcs_simple['c&dh_standard'] = True
aodcs_simple['c&dh_optim'] = True
aodcs_simple['struct_stand'] = True
aodcs_simple['struct_high_resist'] = True

bus_vs_bus.append(aodcs_simple)



prop_elect = {}
prop_elect['name'] = 'Electric Propulsion'
prop_elect['slug'] = 'prop-elect'
prop_elect['therm_active'] = True
prop_elect['therm_passive'] = True
prop_elect['pow_prim_panels'] = True
prop_elect['pow_prim_rtg'] = True
prop_elect['pow_sec_batt'] = True
prop_elect['pow_sec_fc'] = False
prop_elect['comm_mono'] = True
prop_elect['comm_omni'] = True
prop_elect['aodcs_robust'] = True
prop_elect['aodcs_simple'] = True
prop_elect['prop_electr'] = True
prop_elect['prop_chem'] = False
prop_elect['c&dh_standard'] = True
prop_elect['c&dh_optim'] = True
prop_elect['struct_stand'] = True
prop_elect['struct_high_resist'] = True

bus_vs_bus.append(prop_elect)



prop_chem = {}
prop_chem['name'] = 'Chemical Propulsion'
prop_chem['slug'] = 'prop-chem'
prop_chem['therm_active'] = True
prop_chem['therm_passive'] = True
prop_chem['pow_prim_panels'] = True
prop_chem['pow_prim_rtg'] = True
prop_chem['pow_sec_batt'] = True
prop_chem['pow_sec_fc'] = True
prop_chem['comm_mono'] = True
prop_chem['comm_omni'] = True
prop_chem['aodcs_robust'] = True
prop_chem['aodcs_simple'] = False
prop_chem['prop_electr'] = False
prop_chem['prop_chem'] = True
prop_chem['c&dh_standard'] = True
prop_chem['c&dh_optim'] = True
prop_chem['struct_stand'] = True
prop_chem['struct_high_resist'] = True

bus_vs_bus.append(prop_chem)



cdh_standard = {}
cdh_standard['name'] = 'C&DH Standard'
cdh_standard['slug'] = 'c&dh-standard'
cdh_standard['therm_active'] = True
cdh_standard['therm_passive'] = True
cdh_standard['pow_prim_panels'] = True
cdh_standard['pow_prim_rtg'] = True
cdh_standard['pow_sec_batt'] = True
cdh_standard['pow_sec_fc'] = True
cdh_standard['comm_mono'] = True
cdh_standard['comm_omni'] = False
cdh_standard['aodcs_robust'] = True
cdh_standard['aodcs_simple'] = True
cdh_standard['prop_electr'] = True
cdh_standard['prop_chem'] = True
cdh_standard['c&dh_standard'] = True
cdh_standard['c&dh_optim'] = False
cdh_standard['struct_stand'] = True
cdh_standard['struct_high_resist'] = True

bus_vs_bus.append(c&dh_standard)



cdh_optim = {}
cdh_optim['name'] = 'C&DH Optimized'
cdh_optim['slug'] = 'c&dh-optim'
cdh_optim['therm_active'] = True
cdh_optim['therm_passive'] = True
cdh_optim['pow_prim_panels'] = True
cdh_optim['pow_prim_rtg'] = True
cdh_optim['pow_sec_batt'] = True
cdh_optim['pow_sec_fc'] = True
cdh_optim['comm_mono'] = True
cdh_optim['comm_omni'] = True
cdh_optim['aodcs_robust'] = True
cdh_optim['aodcs_simple'] = True
cdh_optim['prop_electr'] = True
cdh_optim['prop_chem'] = True
cdh_optim['c&dh_standard'] = False
cdh_optim['c&dh_optim'] = True
cdh_optim['struct_stand'] = True
cdh_optim['struct_high_resist'] = True

bus_vs_bus.append(c&dh_optim)



struct_stand = {}
struct_stand['name'] = 'Standard Structure'
struct_stand['slug'] = 'struct-stand'
struct_stand['therm_active'] = True
struct_stand['therm_passive'] = True
struct_stand['pow_prim_panels'] = True
struct_stand['pow_prim_rtg'] = False
struct_stand['pow_sec_batt'] = True
struct_stand['pow_sec_fc'] = True
struct_stand['comm_mono'] = True
struct_stand['comm_omni'] = True
struct_stand['aodcs_robust'] = True
struct_stand['aodcs_simple'] = True
struct_stand['prop_electr'] = True
struct_stand['prop_chem'] = True
struct_stand['c&dh_standard'] = True
struct_stand['c&dh_optim'] = True
struct_stand['struct_stand'] = True
struct_stand['struct_high_resist'] = False

bus_vs_bus.append(struct_stand)


struct_stand = {}
struct_high_resist['name'] = 'Standard Structure'
struct_high_resist['slug'] = 'struct-high_resist'
struct_high_resist['therm_active'] = True
struct_high_resist['therm_passive'] = True
struct_high_resist['pow_prim_panels'] = True
struct_high_resist['pow_prim_rtg'] = True
struct_high_resist['pow_sec_batt'] = True
struct_high_resist['pow_sec_fc'] = True
struct_high_resist['comm_mono'] = True
struct_high_resist['comm_omni'] = True
struct_high_resist['aodcs_robust'] = True
struct_high_resist['aodcs_simple'] = True
struct_high_resist['prop_electr'] = True
struct_high_resist['prop_chem'] = True
struct_high_resist['c&dh_standard'] = True
struct_high_resist['c&dh_optim'] = True
struct_high_resist['struct_stand'] = False
struct_high_resist['struct_high_resist'] = True

bus_vs_bus.append(struct_high_resist)


num_pl_vs_bus = []

num1 = {}
num1['name'] = 'One Payload'
num1['slug'] = 'num1'
num1['therm_active'] = True
num1['therm_passive'] = True
num1['pow_prim_panels'] = True
num1['pow_prim_rtg'] = True
num1['pow_sec_batt'] = True
num1['pow_sec_fc'] = False
num1['comm_mono'] = True
num1['comm_omni'] = True
num1['aodcs_robust'] = True
num1['aodcs_simple'] = True
num1['prop_electr'] = True
num1['prop_chem'] = True
num1['c&dh_standard'] = True
num1['c&dh_optim'] = True
num1['struct_stand'] = True
num1['struct_high_resist'] = True

num_pl_vs_bus.append(num1)

num2 = {}
num2['name'] = 'Two Payloads'
num2['slug'] = 'num2'
num2['therm_active'] = True
num2['therm_passive'] = True
num2['pow_prim_panels'] = True
num2['pow_prim_rtg'] = True
num2['pow_sec_batt'] = True
num2['pow_sec_fc'] = False
num2['comm_mono'] = True
num2['comm_omni'] = True
num2['aodcs_robust'] = True
num2['aodcs_simple'] = True
num2['prop_electr'] = True
num2['prop_chem'] = True
num2['c&dh_standard'] = True
num2['c&dh_optim'] = True
num2['struct_stand'] = True
num2['struct_high_resist'] = True

num_pl_vs_bus.append(num2)


num3 = {}
num3['name'] = 'Three Payloads'
num3['slug'] = 'num3'
num3['therm_active'] = True
num3['therm_passive'] = True
num3['pow_prim_panels'] = True
num3['pow_prim_rtg'] = True
num3['pow_sec_batt'] = True
num3['pow_sec_fc'] = True
num3['comm_mono'] = True
num3['comm_omni'] = True
num3['aodcs_robust'] = True
num3['aodcs_simple'] = True
num3['prop_electr'] = True
num3['prop_chem'] = True
num3['c&dh_standard'] = True
num3['c&dh_optim'] = True
num3['struct_stand'] = True
num3['struct_high_resist'] = True

num_pl_vs_bus.append(num3)


num4 = {}
num4['name'] = 'Four Payloads'
num4['slug'] = 'num4'
num4['therm_active'] = True
num4['therm_passive'] = True
num4['pow_prim_panels'] = True
num4['pow_prim_rtg'] = True
num4['pow_sec_batt'] = True
num4['pow_sec_fc'] = True
num4['comm_mono'] = True
num4['comm_omni'] = True
num4['aodcs_robust'] = True
num4['aodcs_simple'] = True
num4['prop_electr'] = True
num4['prop_chem'] = True
num4['c&dh_standard'] = False
num4['c&dh_optim'] = True
num4['struct_stand'] = True
num4['struct_high_resist'] = True

num_pl_vs_bus.append(num4)

num5 = {}
num5['name'] = 'Five Payloads'
num5['slug'] = 'num5'
num5['therm_active'] = True
num5['therm_passive'] = True
num5['pow_prim_panels'] = True
num5['pow_prim_rtg'] = True
num5['pow_sec_batt'] = True
num5['pow_sec_fc'] = True
num5['comm_mono'] = True
num5['comm_omni'] = True
num5['aodcs_robust'] = True
num5['aodcs_simple'] = True
num5['prop_electr'] = True
num5['prop_chem'] = True
num5['c&dh_standard'] = False
num5['c&dh_optim'] = True
num5['struct_stand'] = True
num5['struct_high_resist'] = True

num_pl_vs_bus.append(num5)






















