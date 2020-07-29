import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path 

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Safwan Nisar'
email['to'] = 'safwannisarahmed-sis@scholars.edu.in'
email['subject'] = 'Hello Mr.Nisar'

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
  smtp.ehlo()
  smtp.starttls()
  smtp.login('asafwan752@gmail.com', 'safwan2007')
  smtp.send_message(email)
  print('all good boss!')