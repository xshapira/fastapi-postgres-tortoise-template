import os

from dotenv import load_dotenv


# Load values from the .env file
load_dotenv()

# Project
PROJECT_NAME='Example App'

# Project folders
# TODO

RECREATE_DATABASE=os.environ.get('RECREATE_DATABASE', 'FALSE') == 'TRUE'
