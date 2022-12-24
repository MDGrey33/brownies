# Working with emails
import smtplib
smtp_object = smtplib.SMTP('0.0.0.0', 1025)
print(smtp_object.ehlo())

from_address = 'from@senderdomain.com'
to_address = 'to@receiver.com'
message = 'Subject: this is a test email from pychatm \n hey this is the body of the email'
smtp_object.sendmail(from_address, to_address, message)
