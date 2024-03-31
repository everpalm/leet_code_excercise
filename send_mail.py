#!/usr/bin/python

import smtplib
import sys


sender = 'god@heaven.org'
receivers = (sys.argv[1].split(','))
message1 = """ Alert by my-test <god@heaven.org>
To:"""
message2 = ''
for text_line in receivers:
    message2 += f'{text_line} '
message3 = """
Subject: My test notification

I'm going to convey any messages.
"""
message = message1 + message2 + message3
try:
    smtpObj = smtplib.SMTP('localhost.heaven.org')
    smtpObj.sendmail(sender, receivers, message)
    print("Successfully send email")
except SMTPException:
    print ("Error: unable to send email")