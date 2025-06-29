from os import environ as env
import os

# App Config
US_STATE_RAW = os.environ.get('US_STATE')

if not US_STATE_RAW:
    raise RuntimeError("Variável de ambiente US_STATE não definida")

US_STATE = ' '.join(word.capitalize() if len(word) > 0 else word for word in US_STATE_RAW.split())

PORT = int(env.get("PORT", 5000))
DEBUG_MODE = int(env.get("DEBUG_MODE", 1))

# AWS Info
AWS_REGION = os.environ.get('AWS_REGION')
AWS_BUCKET = os.environ.get('AWS_BUCKET')
AWS_DYNAMODB_TABLE = os.environ.get('AWS_DYNAMODB_TABLE')

# Gunicorn config
bind = ":" + str(PORT)
# workers = multiprocessing.cpu_count() * 2 + 1
# threads = 2 * multiprocessing.cpu_count()