from django.conf import settings
from django.core.mail import send_mail

def send_email(email , token, username):
    try:
        subject = 'your account need to be verify'
        message = f'hi {username}  please contact us in this contact number as soon as possible *********'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email ]
        send_mail( subject, message, email_from, recipient_list )

        
    except Exception as e:
        return False
    
    return True