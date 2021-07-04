from jinja2 import Template
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from password import password

sender_name = "Quizbot <patricksmyth01@gmail.com>"
sender_email = "patricksmyth01@gmail.com"


def send_mail(receiver_email, receiver_name, date, day):



    # receiver_email = "patricksmyth01@gmail.com"


    message = MIMEMultipart("alternative")

    if day == 'monday':
        message["Subject"] = f"Calling All Quizzards! Can You Quiz on {date}?"
    else:
        raise "Not a valid day, needs to be monday or wednesday"


    
    message["From"] = sender_name
    message["To"] = receiver_email


    text = 'Plain text version'


    jinja2_template_string = open("templates/monday.html", 'r').read()
    template = Template(jinja2_template_string)

    html = template.render(email=receiver_email,
                           name=receiver_name,
                           date='1/17/21')



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


send_mail('patricksmyth01@gmail.com', "Patrick", '7/3/21', 'monday')
