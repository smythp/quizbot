import os
import random

from sendy import send_mail
import datetime
import csv
import sys
from password import password

TEST = True

args = sys.argv


if TEST == True:
    sendee = "patricksmyth01@gmail.com"
else:    
    sendee = "ann.pedtke@gmail.com"


subject = "Please buy some milk today!"
files = []
body = """This is an email to remind you to buy some lovely whole milk for the apartment.


With affection,
Milkbot"""


send_mail("Your Local Milkbot", sendee, subject, body, files, server="smtp.gmail.com", port=587, username='patricksmyth01@gmail.com', password=password, isTls=True)


