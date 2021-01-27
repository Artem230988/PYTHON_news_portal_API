from django.core.mail import send_mail
from django.conf import settings


def my_send_mail(text_mail, to_whom):
    send_mail('*************** News_portal INFO ***************', text_mail, settings.EMAIL_HOST_USER, to_whom, fail_silently=False)
