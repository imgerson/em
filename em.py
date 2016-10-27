#!/usr/bin/env python3


import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


class ConfigEm:
    user = None
    password= None


class Em:
    msg = None
    conf = None

    def __init__(self, conf):
        self.conf = conf
        self.msg = MIMEMultipart()

    def attach(self, attachment):
        attachment_name = os.path.basename(attachment)
        attachment_obj = open(attachment, 'rb')

        attachment = MIMEBase('application', 'octet-stream')
        attachment.set_payload((attachment_obj).read())
        encoders.encode_base64(attachment)
        attachment.add_header('Content-Disposition',
            'attachment; filename = {}'.format(attachment_name))

        self.msg.attach(attachment)

    def send(self, toaddr, subject, message):
        self.msg['From'] = self.conf.user
        self.msg['To'] = toaddr
        self.msg['Subject'] = subject
        self.msg.attach(MIMEText(message, 'plain'))

        msg_as_string = self.msg.as_string()

        if self.server:
            self.server.sendmail(self.conf.user, toaddr, msg_as_string)
        else:
            raise EnvironmentError('Not connection to server')

    def login(self):
        self.server = smtplib.SMTP('smtp.gmail.com')
        self.server.starttls()
        self.server.login(self.conf.user, self.conf.user_password)

    def logout(self):
        self.server.quit()
