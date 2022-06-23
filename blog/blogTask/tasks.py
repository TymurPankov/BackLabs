from celery import shared_task
from django.core.mail import send_mail
from .models import EmailUserSend
from chat.models import Message
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from datetime import datetime, timezone


@shared_task(name="my_first_task")
def my_first_task():
   email_list = list(EmailUserSend.objects.all().values_list("user__email", flat=True))

   subject = 'Sending emails using celery'

   message = 'Hello this is my first send email with celery using Django'

   send_mail(subject, message, None, email_list)
   now = datetime.now(timezone.utc).strftime("%m/%d/%Y, %H:%M:%S")
   channel_layer = get_channel_layer()
   async_to_sync(channel_layer.group_send)(
      'taskGroup',
      {
         'type': 'taskEmail',
         'name': 'Mailing',
         'dateEnd': now,
         'result': f'{EmailUserSend.objects.all().count()} mails was sent'
      }
   )


@shared_task(name="messageDelete")
def messageDelete():
   count = Message.objects.all().delete()
   print("Deleted")
   now = datetime.now(timezone.utc).strftime("%m/%d/%Y, %H:%M:%S")
   channel_layer = get_channel_layer()
   async_to_sync(channel_layer.group_send)(
      'taskGroup',
      {
         'type': 'taskDelMes',
         'name': 'Delete chat messages',
         'dateEnd': now,
         'result': f'Deleted {count[0]} messages'
      }
   )