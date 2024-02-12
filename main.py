import requests
import ollama
import os

# Retrieve GitHub API key and username from environment variables
GITHUB_API_KEY = os.getenv('GITHUB_API_KEY', 'default_api_key_if_any')
GITHUB_USERNAME = os.getenv('GITHUB_USERNAME', 'Cdaprod')

def get_github_contributions(username):
    """Fetch recent public contributions of a user from GitHub."""
    url = f'https://api.github.com/users/{username}/events/public'
    headers = {'Authorization': f'token {GITHUB_API_KEY}'}
    response = requests.get(url, headers=headers)
    events = response.json()
    
    contributions = []
    for event in events:
        if event['type'] == 'PushEvent':
            repo_name = event['repo']['name']
            commit_msgs = [commit['message'] for commit in event['payload']['commits']]
            contributions.append({'repo_name': repo_name, 'commit_msgs': commit_msgs})
    
    return contributions

def summarize_contributions(contributions):
    """Use the Ollama library to generate a summarized listing of contributions."""
    contributions_text = '\n'.join([f"Repository {c['repo_name']} had commits: {'; '.join(c['commit_msgs'])}" for c in contributions])
    response = ollama.chat(
        model='llama2',
        messages=[{'role': 'user', 'content': f"Summarize these GitHub contributions: {contributions_text}"}]
    )
    return response['message']['content']

def main():
    contributions = get_github_contributions(GITHUB_USERNAME)
    summary = summarize_contributions(contributions)
    print(summary)

if __name__ == '__main__':
    main()