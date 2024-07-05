
import datetime
import requests
from config.settings import TELEGRAM_URL, TELEGRAM_TOKEN
from habit.models import Habit
from habit.services import message_create, name_of_user, send_tg
from celery import shared_task

@shared_task
def send_message_tg():

    current_time = datetime.datetime.now().strftime("%X")

    habits = Habit.objects.all()

    for habit in habits:
        if habit.time == current_time:
            print("Время пришло!")
        else:
            print("Немного подождем...")
            text_message = message_create(habit.pk)
            chat_id = habit.creator.chat_id

            print(text_message)
            print(chat_id)



