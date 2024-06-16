from flask import Flask, request, jsonify
from src.github_fetcher import get_repo_data, save_to_file
from src.route_optimizer import dijkstra, a_star
from src.data_fetcher import fetch_osm_data, fetch_simulated_ride_sharing_data

app = Flask(__name__)

@app.route('/')
def index():
    return "Ride-Sharing Optimization Engine"

@app.route('/fetch_repo', methods=['POST'])
def fetch_repo():
    data = request.json
    owner = data.get('owner')
    repo = data.get('repo')
    access_token = data.get('access_token')
    
    repo_data = get_repo_data(owner, repo, access_token)
    if repo_data:
        save_to_file(repo_data, 'repo_data.json')
        return jsonify(repo_data)
    else:
        return jsonify({'error': 'Failed to fetch repository data'}), 400

@app.route('/optimize_route', methods=['POST'])
def optimize_route():
    data = request.json
    graph = data.get('graph')
    start = data.get('start')
    end = data.get('end')
    locations = data.get('locations')
    algorithm = data.get('algorithm', 'dijkstra')
    
    if algorithm == 'dijkstra':
        cost, path = dijkstra(graph, start, end)
    elif algorithm == 'a_star':
        cost, path = a_star(graph, start, end, locations)
    else:
        return jsonify({'error': 'Unsupported algorithm'}), 400
    
    return jsonify({'cost': cost, 'path': path})

@app.route('/fetch_osm_data', methods=['GET'])
def fetch_osm():
    bbox = request.args.get('bbox')
    if bbox:
        fetch_osm_data(bbox)
        return jsonify({'message': 'OSM data fetched successfully'}), 200
    else:
        return jsonify({'error': 'Bounding box is required'}), 400

@app.route('/fetch_simulated_data', methods=['GET'])
def fetch_simulated_data():
    fetch_simulated_ride_sharing_data()
    return jsonify({'message': 'Simulated ride-sharing data fetched successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)
