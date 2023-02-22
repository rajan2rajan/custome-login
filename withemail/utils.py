from django.conf import settings
from django.core.mail import send_mail


# token while login 
def send_login_token(email , token, username):
    try:
        subject = 'your account need to be verify'
        message = f'Hi {username} thank you for registering in geeksforgeeks.  http://127.0.0.1:8000/verify/{token}'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email ]
        send_mail( subject, message, email_from, recipient_list )

        
    except Exception as e:
        return False
    
    return True


# token while changing password with old password
def send_password_token(email , token):
    try:
        subject = 'your account need to be verify'
        message = f'hi to change password please click in the link .  http://127.0.0.1:8000/newpassword/{email}/{token}'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email ]
        send_mail( subject, message, email_from, recipient_list )

        
    except Exception as e:
        return False
    
    return True









def send(link,email):
    try:
        subject = 'your account need to be verify'
        message = f'Hi thank you for registering in geeksforgeeks. {link}'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email ]
        send_mail( subject, message, email_from, recipient_list )

        
    except Exception as e:
        return False
    
    return True