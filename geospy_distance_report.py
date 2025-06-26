import pandas as pd
from geopy.distance import geodesic
import folium
import os

# Read vehicle data from Excel
df = pd.read_excel("vehicle_locations.xlsx")

# Prepare map
if len(df) < 2:
    raise ValueError("Need at least two vehicles for comparison.")

# Create folium map centered on the midpoint of first two coordinates
lat1, lon1 = df.iloc[0]["Latitude"], df.iloc[0]["Longitude"]
lat2, lon2 = df.iloc[1]["Latitude"], df.iloc[1]["Longitude"]
midpoint = [(lat1 + lat2)/2, (lon1 + lon2)/2]
map_obj = folium.Map(location=midpoint, zoom_start=5)

report_lines = []
# Compare all pairs of vehicles
for i in range(len(df)):
    for j in range(i+1, len(df)):
        coord1 = (df.iloc[i]["Latitude"], df.iloc[i]["Longitude"])
        coord2 = (df.iloc[j]["Latitude"], df.iloc[j]["Longitude"])
        vehicle1 = df.iloc[i]["Vehicle_ID"]
        vehicle2 = df.iloc[j]["Vehicle_ID"]
        distance = geodesic(coord1, coord2).kilometers
        report_lines.append(f"{vehicle1} <-> {vehicle2}: {distance:.2f} km")
        # Add markers
        folium.Marker(coord1, tooltip=vehicle1, icon=folium.Icon(color='red')).add_to(map_obj)
        folium.Marker(coord2, tooltip=vehicle2, icon=folium.Icon(color='blue')).add_to(map_obj)
        # Line between them
        folium.PolyLine([coord1, coord2], color="green", weight=2.5).add_to(map_obj)

# Save map and report
map_obj.save("vehicle_map.html")
with open("vehicle_report.txt", "w") as f:
    f.write("GeoSpy Vehicle Distance Report\n------------------------------\n")
    f.write("\n".join(report_lines))