import smtplib
from email.mime.text import MIMEText

body = "This is test email from Pycharmm Ubuntu. How Are you you?"

msg = MIMEText(body)
msg['from'] = 'kumarisamolirani@gmail.com'
msg['to'] = 'prosenjitearnkumar@gmail.com'
msg['subject'] = "Hello, I'm fromm Pycharm"

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("kumarisamolirani@gmail.com", "#samoli123")
server.send_message(msg)
print("Email sent successfully")
server.quit()