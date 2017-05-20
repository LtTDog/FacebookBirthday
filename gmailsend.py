# -*- coding: utf-8 -*-
import smtplib
import datetime as dt

gmail_password = "" # need App Password get it from https://support.google.com/accounts/answer/185833
gmail_user = ""

def mailHandler(to, body):
    if gmail_password == "":
        print("No password set in gmailsend.py")
        return
    
    subject = 'Happy Birthday Script on facebook ' + dt.datetime.today().strftime("%m/%d/%Y")
    # this bit here is just send an email to the main gmail account if facebook account is different, that way if you set it up for someone else facebook it alert you its still running 
    if to != gmail_user:
        to = [gmail_user, to]
    else:
        to = gmail_user
    
    header = 'From: %s\n' % sent_from
    header += 'To: %s\n' % to
    header += 'Subject: %s\n' % subject

    email_text = header + body

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, email_text)
        server.close()
        
        print('Email sent!')
    except Exception as e:
        print('Something went wrong...')
        print(repr(e))


def mailsend(to, posted):
    body = 'I sucessfully posted happy birthday on ' + to + ' facebook for ' + posted + " people"
    mailHandler(to, body)

def mailerror(to, e):
    body = 'I failed posted happy birthday on facebook for the error is \n\n' + repr(e)
    mailHandler(to, body)