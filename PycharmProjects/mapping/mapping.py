import folium

Map = folium.Map(location=[12.984, 77.512], zoom_start=20)
Map.add_child(folium.Marker(location=[12.10, 77.7], popup="Hai i am a Marker", icon=folium.Icon(color='green')))
Map.save("Map1.html")
