import folium
import requests
import openrouteservice as ors
import math as mt



def runningRoute(startLat, startLon, endLat, endLon):

    endpoint = 'https://api.openrouteservice.org/v2/directions/foot-hiking'
    params = {
        'api_key': '5b3ce3597851110001cf6248a856c6e73f4c4ad1aef9e36678da6265',
        'start': f'{startLon},{startLat}',
        'end': f'{endLon},{endLat}',
        'format': 'geojson'}

    response = requests.get(endpoint, params=params).json()

    coords = ((startLon, startLat),(endLon, endLat))

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
            roundtrip = 2*route_len
        except:
            pass
    routeName = "FILLER" #DO THIS

    print("We have generated your perfect running route.")
    print("To access the route, navigate to your files and search 'map.html.'")
    print("When you click on the file, it will open in a tab on your browser.") 
    print("The route matched to you is called ", routeName, ". It is approximately", route_len, "miles each way, so ",roundtrip, "miles total.")
    
    map = folium.Map(location=[startLat,startLon], zoom_start=14)

    folium.Marker(location=[startLat,startLon], icon=folium.Icon(color='green')).add_to(map)
    folium.Marker(location=[endLat, endLon], icon=folium.Icon(color='red')).add_to(map)

    route_line = folium.PolyLine(route_coords, color='blue', weight=8, opacity=0.8)
    route_line.add_to(map)
    map.save('map.html')

runningRoute (39.9810, -75.1552, 40.004207, -75.187436)




#TEMPLE TO ART MUSEUM (39.9810, -75.1552, 39.9654, -75.1806)
    #ATTRIBUTES:
    #4 MILES
    #city
   
#TEMPLE TO RITTENHOUSE (39.9810, -75.1552, 39.9497, -75.1714)
    #5 miles
    #City

#TEMPLE TO FISHTOWN (39.9810, -75.1552, 39.971118, -75.134456)

#TEMPLE TO LAUREL HILL CEMETERY (39.9810, -75.1552, 40.004207, -75.187436)
 #5 miles
 #Nature
#TEMPLE TO PENN'S TREATY
#TEMPLE TO THE ZOO
#TEMPLE ACROSS BEN FRANKLIN BRIDGE
    #ATTRIBUTES:
#TEMPLE TO CITY HALL

#USER INPUTS
#mileage = int(input("How many miles would you like to run? Enter an integer between 3 and 10 "))
#scenery = input("Do you want your run to feature more nature or city? Enter '1' for nature and '2' for city ")

#TO DO:
#provide directions for the routes
#create names for the roots
#create code to match the input to a run
#rounding off the mileage


