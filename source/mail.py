import os
from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_mail(to, subject, body):
    ID = 'k.mikami.sys24@morijyobi.ac.jp'
    PASS = os.environ['MAIL_PASS']
    HOST = 'smtp.gmail.com'
    PORT = 587
    
    msg = MIMEMultipart()
    
    msg.attach(MIMEText(body, 'plain'))
    
    msg['Subject'] = subject
    msg['From'] = ID
    msg['To'] = to
    
    #ここから送信処理
    server = SMTP(HOST, PORT)
    server.starttls()
    server.login(ID, PASS)
    
    server.send_message(msg)
    server.quit()