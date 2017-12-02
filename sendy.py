from password import password
import smtplib, os
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from email import encoders


def send_mail(send_from, send_to, subject, text, files=[], server="localhost", port=587, username='', password=password, isTls=True):
    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = send_to
    msg['Date'] = formatdate(localtime = True)
    msg['Subject'] = subject

    msg.attach( MIMEText(text) )

    for f in files:
        part = MIMEBase('application', "octet-stream")
        part.set_payload( open(f,"rb").read() )
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="{0}"'.format(os.path.basename(f)))
        msg.attach(part)

    smtp = smtplib.SMTP(server, port)
    if isTls: smtp.starttls()
    smtp.login(username,password)
    smtp.sendmail(send_from, send_to, msg.as_string())
    smtp.quit()

# Gmail Sign In
gmail_sender = 'patricksmyth01@gmail.com'
gmail_passwd = password
gmail_name = 'First Bank of Patrick <patricksmyth01@gmail.com>'

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login(gmail_sender, gmail_passwd)




# def send_email(body, subject):
#     TO = 'patricksmyth01@gmail.com'

#     # Gmail Sign In
#     gmail_sender = 'patricksmyth01@gmail.com'
#     gmail_passwd = password
#     gmail_name = 'First Bank of Patrick <patricksmyth01@gmail.com>'

#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.ehlo()
#     server.starttls()
#     server.login(gmail_sender, gmail_passwd)

#     BODY = '\r\n'.join(['To: %s' % TO,
#                         'From: %s' % gmail_name,
#                         'Subject: %s' % subject,
#                         '', body])

#     try:
#         server.sendmail(gmail_sender, [TO], BODY)
#         print ('email sent')
#     except:
#         print ('error sending mail')

#     server.quit()

# send_email('another test', 'test for you')    
