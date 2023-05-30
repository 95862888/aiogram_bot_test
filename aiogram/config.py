from envparse import env

env.read_envfile()

BOT_TOKEN = env.str('BOT_TOKEN')


RASA_HOST = env.str('RASA_HOST')
RASA_PORT = env.int('RASA_PORT')
RASA_WEBHOOK_PATH = env.str('RASA_WEBHOOK_PATH')
RASA_API_URL = f'{RASA_HOST}:{RASA_PORT}/{RASA_WEBHOOK_PATH}'
