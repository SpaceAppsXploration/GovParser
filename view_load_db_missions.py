    # from NASA_dictionary import missions

    '''
    # Script creazione record in Targets (9)
    for m in missions:
        tot_target = m['pageURL']
        inizio = tot_target.find('Target=')
        fine = tot_target.find('&Era=')
        target = tot_target[inizio+7:fine]
        if not Targets.objects.all().filter(name=target):
            newObj = Targets(name=target, body_type=1, image_url='Empty') # per ora setto tutti i tipi a 1 e le immagini a 'Empty'
            newObj.save()   
    '''
    # Script creazione record in Missions (ca. 252)
    for obj in missions:
        tot_target = obj['pageURL']
        inizio = tot_target.find('Target=')
        fine = tot_target.find('&Era=')
        target = tot_target[inizio+7:fine]
        print target
        
        try:
            destination = Targets.objects.all().filter(name=target)[0]
        except:
            raise 

        era = tot_target[fine+5:]
        if era == 'Past':
            era = 1
        if era == 'Present':
            era = 2
        if era == 'Future':
            era = 3
        if era == 'Concept':
            era = 0

               
        tot_link = obj['link']
        name = obj['name']
        inizio = tot_link.find('&MCode=')
        hashed = tot_link[inizio+7:]
        newObj = Missions(target=destination, era=era, name=name, codename=name, hashed=hashed, image_url=obj['image'])
        newObj.save()

    # Script creazione record in Details (ca. 1200)
    for m in missions_details:
        name = m['name']
        data = m['data']
        mission_to_save = Missions.objects.all().filter(name=name)[0]
        for d in data:
            if 'image_link' in d:
                # type Fact
                to_save = Details(mission=mission_to_save, detail_type=d['type'], header=d['header'],
                    body=d['body'], image_link=d['image_link'])
                to_save.save()
            if 'date' in d:
                # type event (news, headlines, key_dates)
                to_save = Details(mission=mission_to_save, detail_type=d['type'], header=d['header'],
                    body=d['body'], date=datetime.datetime.strptime(d['date'], '%d %b %Y').date())
                to_save.save()
            else:
                #type Goals, accomp
                to_save = Details(mission=mission_to_save, detail_type=d['type'], header=d['header'],
                    body=d['body'])
                to_save.save()
    
    #Caricare missioni ESA
    from data.ESA_MISSIONS_COMPLETE import ESA_missions

    from unicodedata import normalize

    def slug(text, encoding=None,
               permitted_chars='abcdefghijklmnopqrstuvwxyz0123456789_'):
        if isinstance(text, str):
            text = text.decode(encoding or 'ascii')
        clean_text = text.strip().replace(' ', '_').lower()
        while '__' in clean_text:
            clean_text = clean_text.replace('__', '_')
        ascii_text = normalize('NFKD', clean_text).encode('ascii', 'ignore')
        strict_text = map(lambda x: x if x in permitted_chars else '', ascii_text)
        return ''.join(strict_text)
 

    count = 0
    for m in ESA_missions:
        if Missions.objects.all().filter(name=m['name'][0]).first() != None:
            new = Missions.objects.all().filter(name=m['name'][0]).first()
                      
            
        else:
            launch_str = str(m["launches"])
            dates = m["launches"]
            #print m["short_description"]
            for i,e in enumerate(dates):
                if e.find('(failed)'):
                    dates[i] = e.replace('(failed)', '')
            if all(int(i) <= 2000 for i in dates):
                era = 1
            if all(int(i) > 2015 and int(i) < 2020 for i in dates):
                era = 3
            if all(int(i) > 2000 and int(i) <= 2017 for i in dates):
                era = 2
            if all(int(i) > 2020 for i in dates):
                era = 0

            destination = Targets.objects.all().get(name=m["target"])
            new_mission = Missions(image_url=m["mission_image"],
            launch_dates=launch_str,
            name= m["name"][0],
            codename= 'None',
            hashed= slug(m['name'][0]),
            target=destination,
            era=era 
            )
            new_mission.save()
            count = count + 1
            
            new = Missions.objects.all().filter(name=m['name'][0]).first()
            

        #create details
        if m.get('short_description'):
            new_goal= Details(mission=new, detail_type=1, header="Goal",
                body=m["short_description"])
            new_goal.save()
        
        header = m['name'][0]+' Website'
        new_link = Details(mission=new, detail_type=4, header=header , body=m["link"])
        new_link.save()


    # Caricare dettagli missioni ESA
    from data.ESA_output_COMPLETE import missions

    count = 0
    for m in missions:
        name = m['name']
        data = m['data']
        mission_to_save = Missions.objects.all().filter(name=name).first()
        print mission_to_save
        for d in data:
            if d['type'] == 5:
                # type Fact
                to_save = Details(mission=mission_to_save, detail_type=d['type'], date=datetime.datetime.strptime(d['date'], '%d %b %Y').date(),
                    body=d['body'], header='Fact')
                to_save.save()
                count += 1
            if d['type'] == 8 or d['type'] == 1:
                # type event (news, headlines, key_dates)
                to_save = Details(mission=mission_to_save, detail_type=d['type'], header=d['header'],
                    body=d['body'])
                to_save.save()
                count += 1
            if d['type'] == 9 or d['type'] == 10 or d['type'] == 11:
                #type Goals, accomp
                to_save = Details(mission=mission_to_save, detail_type=d['type'], header=d['header'],
                    body=d['body'])
                to_save.save()
                count += 1


    return StreamingHttpResponse(json.dumps({'status': 'finished', 'count': count}), content_type="application/json")


    # Caricare dati planets
    from data.physics import physics
    count = 0
    for p in physics:
        name = p['name']
        obj = Targets.objects.get(name=name)

        if p.get('date'):
           discover = p['date']
        else:
            discover = None
        rings = p['rings']
        light = p['light']
        mass = p['mass']
        diameter = p['diameter']
        density = p['density']
        gravity = p['gravity']
        l_day = p['l_day']
        l_year = p['l_year']
        ecc = p['eccentricity']
        dist = p['distance']
        per = p['perihelion']
        aph = p['aphelion']
        tilt = p['tilt']
        active = p['active']
        atm = p['atmosphere']
        
        newPla = Planets(target=obj, discover=discover, rings=rings, light=light, mass=mass, diameter=diameter, density=density, gravity=gravity, l_day=l_day, l_year=l_year, eccent=ecc, distance=dist, perihelion=per, aphelion=aph, inclination=tilt, active=active, atmosphere=atm)
        newPla.save()
        count += 1