from celery import shared_task

from core.utils import VKNotifier


@shared_task
def send_notification(msg: str):
    notifier = VKNotifier()
    notifier.notify(msg)