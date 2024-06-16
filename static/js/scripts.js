function fetchOSMData() {
    fetch('/fetch_osm_data?bbox=-0.489,51.28,0.236,51.686')
        .then(response => response.json())
        .then(data => console.log(data))
        .catch(error => console.error('Error:', error));
}

function fetchSimulatedData() {
    fetch('/fetch_simulated_data')
        .then(response => response.json())
        .then(data => console.log(data))
        .catch(error => console.error('Error:', error));
}
