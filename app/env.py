import os
from dotenv import load_dotenv

load_dotenv()

ENV_VARIABLES = {
    'OPENAI_API_KEY': os.getenv('OPENAI_API_KEY'),
}