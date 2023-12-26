import os
import time
import psutil # https://pypi.org/project/psutil/
import smtplib # https://docs.python.org/3/library/smtplib.html
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart # https://docs.python.org/3/library/email.examples.html

def send_email(subject, body):
    # Sender and receiver email addresses obtained by local environment variables
    sender_email = os.environ.get('SENDER_EMAIL')
    receiver_email = os.environ.get('RECEIVER_EMAIL')
    
    # Credentials for SMTP2Go obtained by local environment variables
    username = os.environ.get('SMTP_USER')
    password = os.environ.get('SMTP_PASSWORD')
    
    # Create the email message object
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject
    
    # Attach the body to the email
    message.attach(MIMEText(body, 'plain'))
    
    # Connect to the SMTP server and send the email
    with smtplib.SMTP('mail.smtp2go.com', 2525) as server:
        server.ehlo() # Handshake with server
        server.starttls() # Start a secure TLS connection with the server
        server.ehlo() # One more handshake for good measure
        server.login(username, password) # Login to the server
        server.sendmail(sender_email, receiver_email, message.as_string())

def monitor_cpu_threshold(threshold):
    # Check CPU usage
    cpu_usage = psutil.cpu_percent(interval=1)
    
    # If CPU usage exceeds the threshold, send an email alert
    if cpu_usage > threshold:
        subject = 'High CPU Usage Alert!'
        body = f'Current CPU usage: {cpu_usage}%'
        send_email(subject, body)
        print('Email alert sent!')

if __name__ == "__main__":
    # Set the CPU threshold (e.g., 80%)
    threshold = 80
    
    while True:
        # Monitor CPU usage and send an alert if the threshold is exceeded
        monitor_cpu_threshold(threshold)
        time.sleep(5)
