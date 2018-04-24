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

fgv = folium.FeatureGroup(name="volcanoes")

for lt, ln, el in zip(lat, lon, elev):
   fgv.add_child(folium.CircleMarker(location=[lt, ln], radius = 6, popup=str(el)+" m",
   fill_color=color_producer(el), color = 'grey', fill=True, fill_opacity=0.7))

fgp = folium.FeatureGroup(name="population")

# adding GeoJson polygon layer
fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'yellow' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
# Adding a Layer Control Panel
map.add_child(folium.LayerControl())

map.save("map1.html")
