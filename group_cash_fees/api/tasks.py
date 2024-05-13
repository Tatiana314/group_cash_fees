from django.core.mail import send_mail
from celery import shared_task


@shared_task()
def task_send_email_message(subject, email, message):
    send_mail(
        subject=subject,
        message=message,
        from_email="sredawork@gmail.com",
        recipient_list=email,
        fail_silently=True
    )
