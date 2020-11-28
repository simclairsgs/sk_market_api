from django.test import TestCase

# Create your tests here.
def mail_test():
    import smtplib
    sender_email = "sgs.alertsys@gmail.com"
    import base64
    val = b'c2ltY2xhaXIuc2dzQDk0ODczNTQwMzg='
    pwd = base64.b64decode(val).decode('utf-8')
    from django.conf import settings
    receiver = settings.ADMIN_MAIL_ID
    message = 'Hey!! Admin,\n\tThis is a stock remainder for'+'fkhgt'+'.Only few items left - '+ str(4) + '\n Order soon using stock table details from admin page.'+'Neglect the message, if its already done or remove product if wanted.'
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(sender_email,pwd)
    server.sendmail(sender_email,receiver,message)
    print('stock remainder mail sent..to '+receiver)

