
import requests
import json

def get_repo_data(owner, repo, access_token=None):
    url = f"https://api.github.com/repos/{owner}/{repo}"
    headers = {}
    if access_token:
        headers['Authorization'] = f"token {access_token}"
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        repo_data = response.json()
        return repo_data
    else:
        print(f"Failed to fetch data: {response.status_code}")
        return None

def save_to_file(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

def main():
    owner = "YOUR_GITHUB_USERNAME_OR_ORG"
    repo = "YOUR_REPO_NAME"
    access_token = "YOUR_ACCESS_TOKEN"  # Optional: If the repository is private or to increase rate limits

    repo_data = get_repo_data(owner, repo, access_token)
    
    if repo_data:
        save_to_file(repo_data, 'repo_data.json')
        print("Repository data saved to 'repo_data.json'")
    else:
        print("No data retrieved.")

if __name__ == "__main__":
    main()
