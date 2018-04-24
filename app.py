import folium
import pandas

data = pandas.read_csv("Volcanoes_USA.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif elevation < 3000:
        return 'orange'
    else:
        return 'red'

map = folium.Map(location=[38.58,-99.09], zoom_start=5, tiles="Mapbox Bright")

fg = folium.FeatureGroup(name="My map")

for lt, ln, el in zip(lat, lon, elev):
   fg.add_child(folium.CircleMarker(location=[lt, ln], radius = 6, popup=str(el)+" m",
   fill_color=color_producer(el), color = 'grey', fill=True, fill_opacity=0.7))

#adding GeoJson polygon layer
fg.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read()))

map.add_child(fg)

map.save("map1.html")
