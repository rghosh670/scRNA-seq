import smtplib
from datetime import datetime

# datetime object containing current date and time
now = datetime.now()

# mm/dd/YY H:M:S
dt_string = now.strftime("%m/%d/%Y %I:%M:%S %p")

gmail_user = 'uclathrowaway123@gmail.com'
gmail_password = 'Imputation99!'

sent_from = gmail_user
to = ['rohitghosh101@gmail.com']
subject = 'Python ' + dt_string
body = 'Script finished?'

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, email_text)
    server.close()

    print('Email sent!')
except:
    print('Something went wrong...')