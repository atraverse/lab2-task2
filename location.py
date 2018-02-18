import folium
import geocoder

def coordinates(i):
    '''
    (list)->(list)
    Return list with coordinates
    '''
    lst=[]
    for j in i:
        try:
            g = geocoder.google(j)
            g1 = g.latlng
            lst.append(g1)
        except:
            pass
    return lst

def point(loc, friends):
    '''
    Main function, create HTML file and enter information to it
    '''
    if len(friends)<1:
        map2 = folium.Map()
        people = folium.FeatureGroup(name='Friends')
        map2.add_child(people)
        map2.add_child(folium.LayerControl())
        map2.save('template/result.html')
    else:
        lst = coordinates(loc)
        for i in lst:
            if type(i)!="list":
                lst.remove(i)
        map1 = folium.Map(location =lst[0], zoom_start = 4)
        people = folium.FeatureGroup(name='Friends')
        for i, j in zip(lst, friends):
            people.add_child(folium.Marker(location = i, icon = folium.Icon(),
                                            popup = j))
        
        map1.add_child(people)
        map1.add_child(folium.LayerControl())
        map1.save('template/result.html')
#point(['Redmond, WA', 'USA', 'Redmond', 'Seattle, WA', 'Redmond, WA'], ['msretail', 'SamsungMobileUS', 'GabeAul', 'KudoTsunoda', 'windowsinsider'])
