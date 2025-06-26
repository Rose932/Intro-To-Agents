import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
# Retrieve the API key
API_KEY = os.getenv("MISTRAL_API_KEY")

# Ensure the API key is present
if not API_KEY:
    raise ValueError("MISTRAL_API_KEY not found in .env file.")