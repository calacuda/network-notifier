"""
notify.py

this handles notifying people via email (emails to be alerted found in
alert_emails.txt). the file send the email from teh email found in client.txt

good portions of this code was taken from: 
https://learndataanalysis.org/how-to-use-gmail-api-to-send-an-email-in-python/
"""


import pickle
import os
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from google_auth_oauthlib.flow import Flow, InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload
from google.auth.transport.requests import Request


CLIENT_SECRET_FILE = 'client_secret.json'
API_NAME = 'gmail'
API_VERSION = 'v1'
SCOPES = ['https://mail.google.com/']

SUBJECT = "network compremised?"

try:
    with open("tmp_alert_emails.txt", "r") as alert:
        RECIVER = [email.strip() for email in alert.readlines()]
        
    with open("tmp_client_email.txt", "r") as client:
        SENDER = client.readlines()[0]
except FileNotFoundError:
    with open("alert_emails.txt", "r") as alerts:
        RECIVER = [email.strip() for email in alerts.readlines()]
        
    with open("client_email.txt", "r") as client:
        SENDER = client.readlines()[0]


def Create_Service(client_secret_file, api_name, api_version, *scopes):
    print(client_secret_file, api_name, api_version, scopes, sep='-')
    CLIENT_SECRET_FILE = client_secret_file
    API_SERVICE_NAME = api_name
    API_VERSION = api_version
    SCOPES = [scope for scope in scopes[0]]
    print(SCOPES)

    cred = None

    pickle_file = f'token_{API_SERVICE_NAME}_{API_VERSION}.pickle'
    # print(pickle_file)

    if os.path.exists(pickle_file):
        with open(pickle_file, 'rb') as token:
            cred = pickle.load(token)

    if not cred or not cred.valid:
        if cred and cred.expired and cred.refresh_token:
            cred.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
            cred = flow.run_local_server()

        with open(pickle_file, 'wb') as token:
            pickle.dump(cred, token)

    try:
        service = build(API_SERVICE_NAME, API_VERSION, credentials=cred)
        print(API_SERVICE_NAME, 'service created successfully')
        return service
    except Exception as e:
        print('Unable to connect.')
        print(e)
        return None


def send_message(hostnames, subject=SUBJECT, reciver=RECIVER):
    service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
    emailMsg = "There's a new device on your network:\n\n >  " + "\n > ".join(list(hostnames.values))
    messages = []
    mimeMessage = MIMEMultipart()
    for email in reciver:
        mimeMessage['to'] = email
        mimeMessage['subject'] = subject
        mimeMessage.attach(MIMEText(emailMsg, 'plain'))
        raw_string = base64.urlsafe_b64encode(mimeMessage.as_bytes()).decode()
        message = service.users().messages().send(userId='me',
                                                  body={'raw': raw_string}).execute()
        messages.append(message)
    return messages


if __name__ == '__main__':
    send_message("this is a drill")
