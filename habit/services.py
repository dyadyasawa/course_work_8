
import requests
from config.settings import TELEGRAM_TOKEN, TELEGRAM_URL
from habit.models import Habit
from django.http import HttpResponse



def message_create(habit_id):

    habit = Habit.objects.get(id=habit_id)

    user = habit.creator
    time = habit.time
    if habit.place is None:
        place = "Любое место"
    else:
        place = habit.place

    action = habit.action
    tg_id = user.chat_id

    message = f"Доброго времени суток {user}! Пришло время({time})! Необходимо выполнить({action}), в условленном месте({place})."
    response = send_tg(tg_id, message)

    return HttpResponse(response)

def send_tg(chat_id, message):
    params = {
        'text': message,
        'chat_id': chat_id,
    }
    requests.get(f'{TELEGRAM_URL}{TELEGRAM_TOKEN}/sendMessage', params=params)
