import imaplib
import email
from email.header import decode_header
from datetime import datetime

# Configure your email and password
EMAIL = 'anujchoubey918@gmail.com'
PASSWORD = 'rcnfdbvmzjtcusca'
SMTP_SERVER = 'imap.gmail.com'
SMTP_PORT = 993


def connect_to_gmail(email_address, password):
    # Connect to the server
    # print('running')
    mail = imaplib.IMAP4_SSL(SMTP_SERVER, SMTP_PORT)
    mail.login(email_address, password)
    return mail


def get_unseen_emails(mail):
    # mail.select('inbox')
    # status, messages = mail.search(None, 'UNSEEN')
    # return messages[0].split()
    mail.select('inbox')
    # Format today's date in the required format
    today = datetime.today().strftime('%d-%b-%Y')
    # Search for unseen emails received today
    status, messages = mail.search(None,
                                   f'(UNSEEN FROM "info@ccsc.helpersin.com" SUBJECT "Reset Password PIN" ON {today})')
    # print(messages[0].split())
    # print("*************")
    return messages[0].split()


def get_email_body(mail, mail_id):
    status, msg_data = mail.fetch(mail_id, '(RFC822)')
    for response_part in msg_data:
        if isinstance(response_part, tuple):
            msg = email.message_from_bytes(response_part[1])
            if msg.is_multipart():
                for part in msg.walk():
                    if part.get_content_type() == "text/plain":
                        return part.get_payload(decode=True).decode()
            else:
                return msg.get_payload(decode=True).decode()
    return None


def get_forgot_password_email_body(email_address, password):
    mail = connect_to_gmail(email_address, password)
    mail_ids = get_unseen_emails(mail)
    l = []
    for mail_id in mail_ids:
        # print(mail_id)
        status, msg_data = mail.fetch(mail_id, '(RFC822)')
        for response_part in msg_data:
            if isinstance(response_part, tuple):
                msg = email.message_from_bytes(response_part[1])
                mail_subject, encoding = decode_header(msg['Subject'])[0]
                # print(mail_subject)
                # print("#######################")
                if isinstance(mail_subject, bytes):
                    mail_subject = mail_subject.decode(encoding if encoding else 'utf-8')
                    # print(mail_subject)
                if 'Reset Password PIN' in mail_subject:
                    l.append(get_email_body(mail, mail_id))
    print(l)
    return l[-1] if l else l


def extract_pin_code_from_email_body(email_body):
    import re
    match = re.search(r'\b\d{6}\b', email_body)
    if match:
        return match.group(0)
    else:
        raise ValueError("No PIN code found in the email body")

# extract_pin_code_from_email_body()
# Example usage
# email_body = get_forgot_password_email_body(EMAIL, PASSWORD)
# if email_body:
#     print("Email body:\n", email_body)
# else:
#     print("No 'Forgot Password' email found.")
