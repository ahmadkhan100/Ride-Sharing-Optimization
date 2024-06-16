import requests
import pandas as pd

def fetch_osm_data(bbox):
    url = f"https://api.openstreetmap.org/api/0.6/map?bbox={bbox}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.content
        with open('osm_data.xml', 'wb') as file:
            file.write(data)
        print("OSM data saved to 'osm_data.xml'")
    else:
        print(f"Failed to fetch data: {response.status_code}")

def fetch_simulated_ride_sharing_data():
    # Simulated ride-sharing data
    data = {
        'ride_id': [1, 2, 3, 4, 5],
        'start_location': ['A', 'B', 'C', 'D', 'E'],
        'end_location': ['B', 'C', 'D', 'E', 'A'],
        'start_time': ['2024-06-16 08:00', '2024-06-16 09:00', '2024-06-16 10:00', '2024-06-16 11:00', '2024-06-16 12:00'],
        'end_time': ['2024-06-16 08:30', '2024-06-16 09:30', '2024-06-16 10:30', '2024-06-16 11:30', '2024-06-16 12:30'],
        'price': [10.0, 12.5, 8.0, 9.5, 11.0]
    }
    df = pd.DataFrame(data)
    df.to_csv('simulated_ride_sharing_data.csv', index=False)
    print("Simulated ride-sharing data saved to 'simulated_ride_sharing_data.csv'")

if __name__ == "__main__":
    # Bounding box for a specific area (example: London)
    bbox = "-0.489,51.28,0.236,51.686"
    fetch_osm_data(bbox)
    fetch_simulated_ride_sharing_data()

