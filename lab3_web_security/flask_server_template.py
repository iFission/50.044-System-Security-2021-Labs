#!/usr/bin/env python2

from flask import Flask
from flask import request
import smtplib, ssl

app = Flask(__name__)


class Mail:
    def __init__(self):
        self.port = 465
        self.smtp_server_domain_name = "smtp.gmail.com"
        self.sender_mail = "jamesnotalex3@gmail.com"
        self.password = "4865VmcNrmKR2pF"

    def send(self, recipient, subject):
        ssl_context = ssl.create_default_context()
        service = smtplib.SMTP_SSL(self.smtp_server_domain_name,
                                   self.port,
                                   context=ssl_context)
        service.login(self.sender_mail, self.password)

        result = service.sendmail(self.sender_mail, recipient,
                                  "Subject: {}".format(subject))

        service.quit()


@app.route('/', methods=['GET'])
def email_server():
    arg1 = request.args.get('to', None)
    arg2 = request.args.get('payload', None)

    if arg1 is None or arg2 is None:
        return 'Error: Missing parameters'
    else:
        mail = Mail()
        mail.send(arg1, arg2)
        return 'to=' + arg1 + ', payload=' + arg2


app.run(host='127.0.0.1', port=8000, debug=True)
