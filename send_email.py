import smtplib
import ssl

host = "smtp.gmail.com"
port = 465

username = "ogochukwu.ozotta@gmail.com"
password = "ypzavcxqsichjqri"


receiver = "ogochukwu.ozotta@gmail.com"
context = ssl.create_default_context()

message = """\
Subject: Checking
Hi!
How are you doing today?
BYE!
"""
with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)