import folium
import pandas

#The data
data = pandas.read_csv("Volcanoes.txt")

# Pulling out columns from the data
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
name = list(data["NAME"])

def elevation_color(elevation):
    if elevation < 1000:
        return "green"
    elif elevation > 1000 and elevation < 2000:
        return "orange"
    else:
        return "red"

map = folium.Map(location=[37.0902, -95.7129], zoom_start=5, tiles="Stamen Terrain") # The center of the map and how far in to zoom and map type

fg = folium.FeatureGroup(name="My Map")

for lt, ln, el, nam in zip(lat, lon, elev, name):
    fg.add_child(folium.Marker(location=[lt, ln], popup=f"""<strong>{nam}</strong> <br /><a href = "https://www.google.com/search?q={nam}%20Volcano" target="_blank">Search Google""", icon=folium.Icon(color=elevation_color(el))))

fg.add_child

map.add_child(fg)

map.save("Map1.html")