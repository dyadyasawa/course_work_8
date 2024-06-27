
import requests
from config.settings import TELEGRAM_TOKEN, TELEGRAM_URL



def send_tg(chat_id, message):
    params = {
        'text': message,
        'chat_id': chat_id,
    }
    requests.get(f'{TELEGRAM_URL}{TELEGRAM_TOKEN}/sendMessage', params=params)
