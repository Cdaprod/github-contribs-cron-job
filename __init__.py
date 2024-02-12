from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access the environment variables
GITHUB_API_KEY = os.getenv('GITHUB_API_KEY')
GITHUB_USERNAME = os.getenv('GITHUB_USERNAME')