import random
from django.core.mail import EmailMessage

from django_rest_auth import settings
from .models import User,OneTimePassword



def generateOtp():
    otp=""
    for i in range(6):
        otp += str(random.randint(1,9))
    return otp


def send_code_to_user(email):
    Subject = "One time passcode for email verification"
    otp_code =generateOtp()
    print(otp_code)
    user = User.objects.get(email=email)
    current_site = "Tamu Inc"
    email_body = f"Hi{user.first_name} thanks for signing up on {current_site} please verify your email with the \n one time passcode {otp_code}"
    from_email=settings.DEFAULT_FROM_EMAIL

    OneTimePassword.objects.create(user=user,code=otp_code)

    d_mail=EmailMessage(subject=Subject,body=email_body,from_email=from_email,to=[email])

    d_mail.send(fail_silently=True)