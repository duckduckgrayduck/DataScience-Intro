import csv
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(to_email, subject, body):
    username = os.environ.get('SMTP_USER')
    sender_password = os.environ.get('SMTP_PASSWORD')
    sender = os.environ.get('VERIFIED_SENDER')

    # Email setup
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    # Connect to the SMTP server
    with smtplib.SMTP('mail.smtp2go.com', 2525) as server:
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(username, sender_password)

        # Send email
        server.sendmail(sender, to_email, msg.as_string())

def send_reminder_emails():
    # Read recipient data from CSV file
    with open('recipient_data.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            to_email = row['Email']
            subject = 'Reminder: Your Upcoming Event'
            body = f"Dear {row['Name']},\n\nThis is a reminder for your upcoming event on {row['Event Date']}.\n\nBest regards,\nYour Organization"

            # Send email
            send_email(to_email, subject, body)
            print(f"Reminder sent to {to_email}")

if __name__ == "__main__":
    send_reminder_emails()
