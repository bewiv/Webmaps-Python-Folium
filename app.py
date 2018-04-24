import folium
map = folium.Map(location=[30.42403,-9.616783], zoom_start=6, tiles="Mapbox Bright")

fg = folium.FeatureGroup(name="My map")

for coordinate in [[30.1,-9.2],[33.1,-6.2]]:
   fg.add_child(folium.Marker(location=coordinate, popup="Hi I am a marker", icon=folium.Icon('green')))

map.add_child(fg)

map.save("map1.html")
