import os
import re # https://docs.python.org/3/library/re.html
import schedule # https://schedule.readthedocs.io/en/stable/
import time 
import smtplib # https://docs.python.org/3/library/smtplib.html
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders # https://docs.python.org/3/library/email.examples.html

def analyze_failed_password_attempts(log_file_path):
    failed_attempts = []
    # Open our log file for reading
    with open(log_file_path, 'r') as log_file:
        for line in log_file:
            if 'Failed password' in line: # Find lines that have Failed Password on it. 
                # Here we use regular expressions to extract the info we want to format out easier to read log file for sending. 
                match = re.search(r'(?P<timestamp>\w{3}  \d+ \d+:\d+:\d+).* sudo:.*USER=(?P<user>\S+).*COMMAND=/usr/bin/grep \'(?P<reason>Failed password)\' (?P<log_file>\S+)', line)
                if match:
                    timestamp = match.group('timestamp')
                    user = match.group('user')
                    reason = match.group('reason')
                    log_file = match.group('log_file')
                    failed_attempts.append(f"Timestamp: {timestamp}, User: {user}, Reason: {reason}, Log File: {log_file}, Status: Failed")

    return failed_attempts

def send_email(to_email, subject, body, attachment_path):
    """ This should look familiar, it's a very similar send email method """
    username = os.environ.get('SMTP_USER')
    sender_password = os.environ.get('SMTP_PASSWORD')
    sender = os.environ.get('SENDER_EMAIL')

    # Email setup
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    # Attach the file to the email message
    with open(attachment_path, 'rb') as attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f"attachment; filename= {os.path.basename(attachment_path)}")
        msg.attach(part)

    # Connect to the SMTP server and send the email
    with smtplib.SMTP('mail.smtp2go.com', 2525) as server:
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(username, sender_password)

        # Send email
        server.sendmail(sender, to_email, msg.as_string())

def generate_daily_report(log_file_path, report_path):
    """ This method generates our daily report by analyzing our log file and saving it as a new file """
    failed_attempts = analyze_failed_password_attempts(log_file_path)

    with open(report_path, 'w') as report_file:
        for attempt in failed_attempts:
            report_file.write(attempt + '\n')

def main():
    log_file_path = '/var/log/auth.log'
    report_path = 'failed_logins.txt'
    generate_daily_report(log_file_path, report_path)

    # Here we configure the receiver email we want to send the reports to and some other email details. 
    to_email = os.environ.get('RECEIVER_EMAIL')
    subject = 'Daily Failed Login Report'
    body = 'Please find attached the daily failed login report.'

    send_email(to_email, subject, body, report_path)

if __name__ == "__main__":
    # Run the script daily at a specific time. 
    schedule.every().day.at("08:35").do(main)

    while True:
        schedule.run_pending()
        time.sleep(1)
