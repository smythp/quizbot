import datetime
import requests
from io import StringIO
import csv
from jinja2 import Template
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from password import password

sender_name = "Quizbot <patricksmyth01@gmail.com>"
sender_email = "patricksmyth01@gmail.com"





def next_weekday(d, weekday):
    days_ahead = weekday - d.weekday()
    if days_ahead <= 0: # Target day already happened this week
        days_ahead += 7
    return d + datetime.timedelta(days_ahead)


def next_wednesday_string():

    return next_weekday(datetime.date.today(), 2)



def get_current_quizzards():
    r = requests.get('https://docs.google.com/spreadsheets/d/1N_qyPcmDCosCLNd3rdP4dXB9VrWtendAeua1O8IJdBA/export?format=csv&gid=2135530720')

    scsv = r.text

    f = StringIO(scsv)
    reader = csv.DictReader(f, delimiter=',')

    return reader



def send_mail(receiver_email, receiver_name, subject, text, html):

    message = MIMEMultipart("alternative")

    message["Subject"] = subject
    message["From"] = sender_name
    message["To"] = receiver_email

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
            )



def single_monday_email(receiver_email, receiver_name, emails):



    date = next_wednesday_string()

    subject = f"Calling All Quizzards! Can you make it on {date}?"
    
    text = 'Plain text version'


    jinja2_template_string = open("templates/monday_inline.html", 'r').read()
    template = Template(jinja2_template_string)

    html = template.render(email=receiver_email,
                           name=receiver_name,
                           date=date,
                           emails=emails)



    send_mail(receiver_email, receiver_name, subject, text, html)







def send_all_monday_emails():

    quizzards_reader = get_current_quizzards()
    
    quizzards = list(quizzards_reader)

    emails = ''

    for quizzard in quizzards:
        emails += quizzard['Your Email'] + ','    
        

        # print(quizzards)

    for quizzard in quizzards:
        single_monday_email(
            quizzard['Your Email'],
            quizzard['Your Name'],
            emails
            )
        


send_all_monday_emails()        
