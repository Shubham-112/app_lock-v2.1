import smtplib, time

timer = time.localtime()

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

mail = 'dark.bot.lock@gmail.com'
passw = 'darkbot12#'

s = smtplib.SMTP(host='smtp.gmail.com', port=587)
s.starttls()
s.login(mail, passw)

msg = MIMEMultipart()

message = ("Chrome was accessed at {}/{}/{} {}:{}".format(timer.tm_mday, timer.tm_mon, timer.tm_year, timer.tm_hour, timer.tm_min ))

msg['From'] = 'darkBot'
msg['To'] = 'shubham.dwc@gmail.com'
msg['Subject'] = "Alert !! Chrome accessed"
msg.attach(MIMEText(message, 'plain'))
s.send_message(msg)