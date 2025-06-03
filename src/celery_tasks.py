from celery import Celery
from src.mail import create_message, mail

c_app = Celery()

c_app.config_from_object('src.config')

@c_app.task()
def send_email():
    message = create_message(
        recipients=[email], subject="Verify your email", body=html_message
    )

    mail.send_message