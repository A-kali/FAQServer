import smtplib
from email.mime.text import MIMEText
from setup import *


def send_email(title, content):
    message = MIMEText(content, 'plain', 'utf-8')
    message['Subject'] = title
    message['From'] = sender
    message['To'] = receivers[0]

    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)
        smtpObj = smtplib.SMTP_SSL(mail_host)
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        smtpObj.quit()
    except smtplib.SMTPException as e:
        print(e)
        send_email(content, title)


def template(stock_name, stock_id):
    pass
