import imaplib
import email
from email.header import decode_header
from datetime import datetime

class Get_pin_form_gmail:

    def __init__(self):
        self.EMAIL = 'lakheramohini98@gmail.com'
        self.PASSWORD = 'inkiqfgkbvuvinbz'
        self.SMTP_SERVER = 'imap.gmail.com'
        self.SMTP_PORT = 993

    def connect_to_gmail(self):
        # Connect to the server
        mail = imaplib.IMAP4_SSL(self.SMTP_SERVER, self.SMTP_PORT)
        mail.login(self.EMAIL, self.PASSWORD)
        return mail

    def get_unseen_emails(self, mail):
        mail.select('inbox')
        # Format today's date in the required format
        today = datetime.today().strftime('%d-%b-%Y')
        # Search for unseen emails received today
        status, messages = mail.search(None, f'(UNSEEN ON {today})')
        return messages[0].split()

    def get_email_body(self, mail, mail_id):
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

    def get_forgot_password_email_body(self):
        mail = self.connect_to_gmail()
        mail_ids = self.get_unseen_emails(mail)

        for mail_id in mail_ids:
            status, msg_data = mail.fetch(mail_id, '(RFC822)')
            for response_part in msg_data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_bytes(response_part[1])
                    mail_subject, encoding = decode_header(msg['Subject'])[0]
                    if isinstance(mail_subject, bytes):
                        mail_subject = mail_subject.decode(encoding if encoding else 'utf-8')
                    if 'Reset Password PIN' in mail_subject:
                        return self.get_email_body(mail, mail_id)
        return None

# Example usage
forgot_password = Get_pin_form_gmail()
email_body = forgot_password.get_forgot_password_email_body()
if email_body:
    print("Email body:\n", email_body)
else:
    print("No 'Forgot Password' email found.")
