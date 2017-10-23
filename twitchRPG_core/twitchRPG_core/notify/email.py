#!/usr/bin/python3

"""
.. module:: Mail
.. moduleauthor:: Miguel G Rubin <mgrubin@softpoint.es>
"""

import smtplib
import json
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from jinja2 import Environment, FileSystemLoader
# from email.mime.image import MIMEImage

from twitchRPG_core import config


def test_email():
    sendmail('Python3 Test Email',
             'This is a python3 test email')


def sendmail(esubj, emsg):
    """
    Send mail method via SMTP.

    :params esubj: Email subject
    :params emsg: Email message
    """
    msg = MIMEMultipart()
    msg['From'] = config.ALERT_SENDER
    msg['To'] = ", ".join(config.ALERT_RECEIVERS)
    msg['Subject'] = esubj
    msg.attach(MIMEText(emsg))
    mailserver = smtplib.SMTP(config.SMTP_HOST, config.SMTP_PORT)
    mailserver.ehlo()
    mailserver.starttls()
    mailserver.ehlo()
    mailserver.login(config.SMTP_USER, config.SMTP_PASS)
    mailserver.sendmail(config.ALERT_SENDER,
                        config.ALERT_RECEIVERS, msg.as_string())
    mailserver.quit()


def send_email_html(subject, receivers, data, template):
    """
    Send mail mehtod via SMTP using HTML template

    :params subject: Email subject string
    :params recievers: Email receivers list of strings
    :params data: Data to fill in the template
    :params template: Jinja2 template name
    """
    tpl_path = os.path.dirname(os.path.realpath(__file__)) + '/templates/'
    j2_env = Environment(loader=FileSystemLoader(tpl_path))
    msg_content = j2_env.get_template(template).render(data)
    msg = MIMEMultipart()
    msg['From'] = config.ALERT_SENDER
    msg['To'] = ", ".join(receivers)
    msg['Subject'] = subject
    msg.attach(MIMEText(msg_content, 'html'))
    mailserver = smtplib.SMTP(config.SMTP_HOST, config.SMTP_PORT)
    mailserver.ehlo()
    mailserver.starttls()
    mailserver.ehlo()
    mailserver.login(config.SMTP_USER, config.SMTP_PASS)
    mailserver.sendmail(config.ALERT_SENDER, receivers, msg.as_string())
    mailserver.quit()
