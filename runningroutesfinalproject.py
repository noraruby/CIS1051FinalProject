import folium
import requests
import openrouteservice as ors
import math as mt
import os
import subprocess as sb

def cityRoutes (mileage):
    if mileage <= 3: return 'Eastern State Penitentiary', (39.9810, -75.1552, 39.96734965539368, -75.17262188819211)
    elif mileage == 4: return 'Art Museum', (39.9810, -75.1552, 39.9654, -75.1806)
    elif mileage == 5: return 'Rittenhouse', (39.9810, -75.1552, 39.9497, -75.1714)
    elif mileage == 6: return 'Ben Franklin Bridge', (39.9810, -75.1552, 39.950706, -75.122472)
    elif mileage == 7: return 'Chicken Pier', (39.9810, -75.1552, 39.928185, -75.141257)
    elif mileage == 8: return 'Manayunk Bridge', (39.9810, -75.1552, 40.016473, -75.212385)
    elif mileage == 9: return 'FDR Park via Center City', (39.9810, -75.1552, 39.903411, -75.183445)
    else: return 'Navy Yard', (39.9810, -75.1552, 39.894029, -75.178686)


def natureRoutes(mileage):
    if mileage <= 3: return 'Penn\'s Treaty', (39.9810, -75.1552, 39.966848946977095, -75.12905528132588)
    elif mileage == 4: return 'Azalea Garden', (39.9810, -75.1552, 39.968383, -75.182746)
    elif mileage == 5: return 'Laurel Hill Cemetary', (39.9810, -75.1552, 40.004207, -75.187436)
    elif mileage == 6: return 'Fairmount Park', (39.9810, -75.1552, 39.988331, -75.198977)
    elif mileage == 7: return 'Philadelphia Zoo', (39.9810, -75.1552, 39.974882, -75.195706)
    elif mileage == 8: return 'The Woodlands', (39.9810, -75.1552, 39.945640, -75.203511)
    elif mileage == 9: return '100 Steps Wissahickon', (39.9810, -75.1552, 40.023512, -75.201418)
    else: return 'West Laurel Hill Cemetary', (39.9810, -75.1552, 40.013857, -75.227957)


def runningRoute(startLat, startLon, endLat, endLon, routeName):
    #source for initialization information: https://openrouteservice-py.readthedocs.io/en/latest/
    endpoint = 'https://api.openrouteservice.org/v2/directions/foot-hiking'
    params = {
        'api_key': '5b3ce3597851110001cf6248a856c6e73f4c4ad1aef9e36678da6265',
        'start': f'{startLon},{startLat}',
        'end': f'{endLon},{endLat}',
        'format': 'geojson'}

    response = requests.get(endpoint, params=params).json()
    coords = ((startLon, startLat),(endLon, endLat))

    #source for setting up openrouteservice: https://www.youtube.com/watch?v=xBxWuq8SR6k
    client = ors.Client(key='5b3ce3597851110001cf6248a856c6e73f4c4ad1aef9e36678da6265') # Specify your personal API key
    routes = client.directions(coords, profile='cycling-regular')
    geometry = routes['routes'][0]['geometry']
    decoded = ors.convert.decode_polyline(geometry)

    route_coords = list(decoded.values())[1:]
    dummy_list = []
    for route_coord in route_coords[0]:
        route_coord.reverse()
        dummy_list.append(route_coord)
    route_coords[0] = dummy_list

    route_len = 0
    for i in range(len(route_coords[0])):
        try:
            x1, y1 = route_coords[0][i]
            x2, y2 = route_coords[0][i+1]
            dx = (x2 - x1) * 48
            dy = (y2 - y1) * 43
            dz = mt.sqrt((dx**2)+(dy**2))
            route_len += dz
        except:
            pass
    route_len = round(route_len, 2)
    roundtrip = route_len * 2

    print("\tWe have generated your perfect running route.")
    #print("\tTo access the route, navigate to your files and search 'map.html.'")
    #print("\tWhen you click on the file, it will open in a tab on your browser.")
    print("\tThe route matched to you is called "+ routeName + ". It is approximately", route_len, "miles each way, so", roundtrip, "miles total.")
    print('\tThe map will open in your browser briefly.')
    
    # source for automatic file opening: https://www.geeksforgeeks.org/how-to-make-html-files-open-in-chrome-using-python/
    try: #should work on Windows
        os.startfile('map.html')
    except:
        try:
            sb.call(['open', "map.html"])
        except:
            print('Could not open HTML.')

    map = folium.Map(location=[startLat,startLon], zoom_start=14)

    folium.Marker(location=[startLat,startLon], icon=folium.Icon(color='green')).add_to(map)
    folium.Marker(location=[endLat, endLon], icon=folium.Icon(color='red')).add_to(map)

    # source for polylines: https://deparkes.co.uk/2016/06/03/plot-lines-in-folium/
    route_line = folium.PolyLine(route_coords, color='blue', weight=8, opacity=0.8)
    route_line.add_to(map)
    map.save('map.html')

mileage = int(input("- How many miles would you like to run? Enter an integer between 3 and 10. "))
scenery = int(input("- Do you want your run to feature more nature or city? Enter '1' for Nature and '2' for City "))

name = ''

if scenery == 1: # nature routes
    name, coords = natureRoutes(mileage)
else: # city routes
    name, coords = cityRoutes(mileage)

runningRoute(coords[0], coords[1], coords[2], coords[3], name)


'''
3 miles:
    NATURE: Penn's Treaty (39.9810, -75.1552, 39.966848946977095, -75.12905528132588)
    CITY: 'Eastern State Penitentiary', (39.9810, -75.1552, 39.96734965539368, -75.17262188819211)
4 miles:
    CITY: 'Art Museum', (39.9810, -75.1552, 39.9654, -75.1806)
    NATURE: Azalea Garden (39.9810, -75.1552, 39.968383, -75.182746)
5 miles:
    CITY: 'Rittenhouse', (39.9810, -75.1552, 39.9497, -75.1714)
    NATURE: Laurel Hill Cemetary (39.9810, -75.1552, 40.004207, -75.187436)
6 miles:
    CITY: 'Ben Franklin Bridge', (39.9810, -75.1552, 39.950706, -75.122472)
    NATURE: 'Fairmount Park', (39.9810, -75.1552, 39.988331, -75.198977)
7 miles:
   CITY: 'Chicken Pier', (39.9810, -75.1552, 39.928185, -75.141257)
   NATURE: 'Philadelphia Zoo', (39.9810, -75.1552, 39.974882, -75.195706)
8 miles:
   CITY: 'Manayunk Bridge', (39.9810, -75.1552, 40.016473, -75.212385)
   NATURE: 'The Woodlands', (39.9810, -75.1552, 39.945640, -75.203511)
9 miles:
   CITY: 'FDR Park via Center City', (39.9810, -75.1552, 39.903411, -75.183445)
   NATURE: '100 Steps Wissahickon', (39.9810, -75.1552, 40.023512, -75.201418)
10 miles:
   CITY: 'Navy Yard', (39.9810, -75.1552, 39.894029, -75.178686)
   NATURE: 'West Laurel Hill Cemetary', (39.9810, -75.1552, 40.013857, -75.227957)
'''