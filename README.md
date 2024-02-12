# Custom AI Job 
## Fetch Recent GitHub Contributions

README.md

Create a README.md file to explain how to use your repository, including how to build and run the Docker container. Here’s a template:

# GitHub Contributions Summarizer

This project fetches your recent public contributions from GitHub and generates a summarized listing using the Ollama library.

## Status Badge



## Getting Started

### Prerequisites

- Docker
- GitHub account

### Installation

1. Clone the repository:

`git clone https://github.com/Cdaprod/github-contribs-cron-job.git`

2. Navigate to the project directory:

`cd github-contribs-cron-job`

3. Build the Docker image:

`docker build -t github-contributions-summarizer .`

Using in Docker:

When running your Docker container, pass the GitHub API key and username as environment variables using the -e option:

`docker run -e GITHUB_API_KEY=your_github_api_token -e GITHUB_USERNAME=your_github_username github-contributions-summarizer`

Replace my_docker_image with the actual name/tag of your Docker image. This command ensures your script within the Docker container has access to the necessary environment variables without hardcoding them into your image or script.

### Configuration and Environment Variable Methods

- Set your GitHub API key and username in the `.env` file.
- Set your GitHub API key and username in the Github Secrets UI.

## License

This project is licensed under the MIT License - David Cannan Cdaprod 2024

---

---

# GRAVEYARD (to be removed)

# Using `ollama`

Based on the provided Ollama Python library README snippet, you can utilize this library to create a cron job that fetches your recent public contributions from GitHub and generates a summarized listing. Let's revise the Python script to use the Ollama library instead of OpenAI directly. This approach simplifies interacting with the Llama2 model for generating summaries. Here's how you can adjust the script:

### Step 1: Install the Ollama Library

First, ensure you have installed the Ollama library:

```bash
pip install ollama
```

### Step 2: Update the Python Script

Modify the `github_contributions.py` script to use the Ollama library. Here's an updated version of the script:

```python
import requests
import ollama

# Configure your GitHub API key and username
GITHUB_API_KEY = 'your_github_api_key'
GITHUB_USERNAME = 'your_github_username'

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
```

### Step 3: Set Up the Cron Job

The setup for the cron job remains the same as previously described. Use the `crontab -e` command to schedule your script to run once a day at your preferred time.

This script now leverages the Ollama library to process the natural language generation part, simplifying the interaction with the model. Ensure you replace `your_github_api_key` and `your_github_username` with your actual GitHub API key and GitHub username.

# Using `openai`

To achieve your goal, you will need to create a Python script that uses the OpenAI (specifically, Ollama with Llama2 model) API Python SDK for natural language processing and the GitHub API to fetch your recent public contributions. Then, you will set up a cron job to run this script once a day. Here's a step-by-step guide to set this up:

### Step 1: Install Required Libraries

First, ensure you have Python installed on your system. Then, install the necessary libraries by running:

```bash
pip install openai requests
```

### Step 2: Write the Python Script

Create a Python script named `github_contributions.py` with the following content. This script will use the GitHub API to fetch your latest public contributions and then use the Ollama API to generate a summarized response.

```python
import openai
import requests

# Configure your OpenAI and GitHub API keys
OPENAI_API_KEY = 'your_openai_api_key'
GITHUB_API_KEY = 'your_github_api_key'
GITHUB_USERNAME = 'your_github_username'

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
    """Use the Ollama API to generate a summarized listing of contributions."""
    openai.api_key = OPENAI_API_KEY
    contributions_text = '\n'.join([f"Repository {c['repo_name']} had commits: {'; '.join(c['commit_msgs'])}" for c in contributions])
    response = openai.ChatCompletion.create(
        model="ollama-llama2",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Summarize these GitHub contributions: {contributions_text}"},
        ]
    )
    return response.choices[0].message['content']

def main():
    contributions = get_github_contributions(GITHUB_USERNAME)
    summary = summarize_contributions(contributions)
    print(summary)

if __name__ == '__main__':
    main()
```

### Step 3: Set Up the Cron Job

To schedule this script to run once a day, you can use cron on a Unix-based system (Linux/macOS). Here's how:

1. Open your terminal.
2. Type `crontab -e` to edit your cron jobs.
3. Add the following line to run the script every day at a specific time (e.g., 8 AM):

```cron
0 8 * * * /usr/bin/python3 /path/to/your/script/github_contributions.py
```

Replace `/path/to/your/script/github_contributions.py` with the actual path to your Python script and `/usr/bin/python3` with the path to your Python interpreter if it's different.

Make sure to replace placeholder values like `your_openai_api_key`, `your_github_api_key`, and `your_github_username` with your actual OpenAI API key, GitHub API key, and GitHub username.

This setup will fetch your recent contributions from GitHub daily and use the Ollama model to summarize them in a natural, conversational way.