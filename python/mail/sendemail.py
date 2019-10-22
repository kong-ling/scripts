from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

import smtplib

#from_addr = input('From: ')
#password = input('Password: ')
#to_addr = input('To: ')
from_addr = 'lklk_lklk@163.com'
password = 'hongkong'
to_addr = 'kong.ling@intel.com'

#smtp_server = input('SMTP server: ')
#smtp_server = 'smtp-mail.outlook.com'
smtp_server = 'smtp.163.com'

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

msg = MIMEText('Hello, sent by Python...', 'plain', 'utf-8')
msg['From'] = _format_addr('Python Lover <%s>' % from_addr)
msg['To'] = _format_addr('Ling, Kong <%s>' % to_addr)
msg['Subject'] = Header('Greetings from Ling Kong', 'utf-8')

server = smtplib.SMTP(smtp_server, 587)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
