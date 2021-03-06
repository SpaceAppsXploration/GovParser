# True/False Tables about mission target's distance

bus_vs_dist = []

dist1 = {}				#Sun, Mercury , Venus
dist1['name'] = 'Dist1'
dist1['slug'] = 'dist1'
dist1['range_min'] = 0
dist1['range_max'] = 0.8
dist1['therm_active'] = True
dist1['therm_passive'] = (False, 'Too hot to be passive')
dist1['pow_prim_panels'] = True
dist1['pow_prim_rtg'] = (False, 'You are cloe enough to the Sun to exploit its energy') 
dist1['pow_sec_batt'] = True
dist1['pow_sec_fc'] = True
dist1['comm_mono'] = (False, 'You are close enough to  Earth to use an omnidirectional antenna')
dist1['comm_omni'] = True
dist1['aodcs_robust'] = True
dist1['aodcs_simple'] = True
dist1['prop_electr'] = True
dist1['prop_chem'] = True
dist1['cdh_standard'] = True
dist1['cdh_optim'] = True
dist1['struct_stand'] = True
dist1['struct_high_resist'] = True

bus_vs_dist.append(dist1)

dist2 = {}				#Earth, Moon, Mars
dist2['name'] = 'Dist2'
dist2['slug'] = 'dist2'
dist2['range_min'] = 0.8
dist2['range_max'] = 1.6
dist2['therm_active'] = True
dist2['therm_passive'] = True
dist2['pow_prim_panels'] = True
dist2['pow_prim_rtg'] = (False, 'You are cloe enough to the Sun to exploit its energy') 
dist2['pow_sec_batt'] = True
dist2['pow_sec_fc'] = True
dist2['comm_mono'] = (False, 'You are close enough to  Earth to use an omnidirectional antenna')
dist2['comm_omni'] = True
dist2['aodcs_robust'] = True
dist2['aodcs_simple'] = True
dist2['prop_electr'] = True
dist2['prop_chem'] = True
dist2['cdh_standard'] = True
dist2['cdh_optim'] = True
dist2['struct_stand'] = True
dist2['struct_high_resist'] = True

bus_vs_dist.append(dist2)

dist3 = {}				#Asteroids
dist3['name'] = 'Dist3'
dist3['slug'] = 'dist3'
dist3['range_min'] = 1.6
dist3['range_max'] = 3
dist3['therm_active'] = True
dist3['therm_passive'] = (False, 'Too cold to be passive')
dist3['pow_prim_panels'] = True
dist3['pow_prim_rtg'] = (False, 'You are cloe enough to the Sun to exploit its energy')
dist3['pow_sec_batt'] = True
dist3['pow_sec_fc'] = True
dist3['comm_mono'] = True
dist3['comm_omni'] = True
dist3['aodcs_robust'] = True
dist3['aodcs_simple'] = True
dist3['prop_electr'] = True
dist3['prop_chem'] = True
dist3['cdh_standard'] = True
dist3['cdh_optim'] = True
dist3['struct_stand'] = (False, 'You should account for micro-meteorit impacts')
dist3['struct_high_resist'] = True

bus_vs_dist.append(dist3)

dist4 = {}			#Jupiter
dist4['name'] = 'Dist4'
dist4['slug'] = 'dist4'
dist4['range_min'] = 3
dist4['range_max'] = 5.5
dist4['therm_active'] = True
dist4['therm_passive'] = (False, 'Too cold to be passive')
dist4['pow_prim_panels'] = True
dist4['pow_prim_rtg'] = True
dist4['pow_sec_batt'] = True
dist4['pow_sec_fc'] = True
dist4['comm_mono'] = True
dist4['comm_omni'] = (False, 'You are so far that you need to focus your signal exclusively towards Earth')
dist4['aodcs_robust'] = True
dist4['aodcs_simple'] = True
dist4['prop_electr'] = True
dist4['prop_chem'] = True
dist4['cdh_standard'] = True
dist4['cdh_optim'] = True
dist4['struct_stand'] = True
dist4['struct_high_resist'] = True

bus_vs_dist.append(dist4)

dist5 = {}				#Saturn, Titan, Uranus, Neptune, Halley, Kuiper Belt, dwarf planets and beyond!!
dist5['name'] = 'Dist5'
dist5['slug'] = 'dist5'
dist5['range_min'] = 5.5
dist5['range_max'] = 50
dist5['therm_active'] = True
dist5['therm_passive'] = (False, 'Too cold to be passive')
dist5['pow_prim_panels'] = (False, 'Almost... Too far from the Sun to rely only on solar panels')
dist5['pow_prim_rtg'] = True
dist5['pow_sec_batt'] = True
dist5['pow_sec_fc'] = True
dist5['comm_mono'] = True
dist5['comm_omni'] = (False, 'You are so far that you need to focus your signal exclusively towards Earth')
dist5['aodcs_robust'] = True
dist5['aodcs_simple'] = True
dist5['prop_electr'] = True
dist5['prop_chem'] = True
dist5['cdh_standard'] = True
dist5['cdh_optim'] = True
dist5['struct_stand'] = True
dist5['struct_high_resist'] = True

bus_vs_dist.append(dist5)
