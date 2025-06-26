# GeoSpy Vehicle Distance Analyzer 

This project calculates the distance between multiple vehicles using their GPS coordinates (latitude & longitude) from an Excel sheet and visualizes the results on an interactive map.

##  Features
- Reads vehicle coordinates from an Excel file (`vehicle_locations.xlsx`)
- Computes distances between all vehicle pairs
- Generates a report (`vehicle_report.txt`)
- Creates a map (`vehicle_map.html`) showing all vehicle locations and routes

##  Files
- `vehicle_locations.xlsx` – Sample input file with vehicle GPS data
- `geospy_distance_report.py` – Python script to compute distances and generate output
- `vehicle_map.html` – Output map showing all vehicles (generated after running script)
- `vehicle_report.txt` – Output report with pairwise distance information (generated after running script)

##  How to Run

1. **Install dependencies**:
   ```bash
   pip install geopy folium pandas openpyxl
   ```

2. **Run the script**:
   ```bash
   python geospy_distance_report.py
   ```

3. **View the results**:
   - Open `vehicle_map.html` in a browser to see the interactive map.
   - Check `vehicle_report.txt` for distance details.

##  Example
With the provided sample data (New Delhi and Mumbai), the tool will:
- Show markers for both locations
- Draw a connecting line
- Display distance in kilometers

---

Made with  for GPS data visualization.
