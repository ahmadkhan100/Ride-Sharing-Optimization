
# Ride-Sharing Optimization Engine

## Overview
This project aims to develop a scalable optimization engine for a ride-sharing platform. It includes features for route optimization and real-time dynamic pricing based on demand and supply analytics.

## Features
- Fetches geographical data from OpenStreetMap.
- Simulates ride-sharing data.
- Implements Dijkstra and A* algorithms for route optimization.
- Provides a web interface for interaction.

## Setup

### Prerequisites
- Python 3.x
- Virtualenv

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/ahmadkhan100/Ride-Sharing-Optimization/
   cd ride_sharing_optimizer
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scriptsctivate`
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application
1. Start the Flask application:
   ```bash
   python app.py
   ```

2. Access the application in your web browser at `http://127.0.0.1:5000`.

## Usage

### Fetching OSM Data
Send a GET request to `/fetch_osm_data` with the `bbox` parameter to fetch geographical data.

### Fetching Simulated Ride-Sharing Data
Send a GET request to `/fetch_simulated_data` to generate and fetch simulated ride-sharing data.

## Contributing
Feel free to open issues or submit pull requests for any improvements or bug fixes.

## License
This project is licensed under the MIT License.
