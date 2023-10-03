import psutil
from flask import Flask, render_template
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)
# Email configuration
smtp_server = 'smtp.gmail.com'  # SMTP server
smtp_port = 587  # 587 for TLS, 465 for SSL
smtp_username = 'smtp username'  # Your email address
smtp_password = 'Email_password'  # Your email password
recipient_email = 'recipient mail'  # Recipient's email address

def send_email(subject, body):
    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = smtp_username
    msg['To'] = recipient_email
    msg['Subject'] = subject

    # Attach the email body
    msg.attach(MIMEText(body, 'plain'))

    # Connect to the SMTP server and send the email
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Use TLS for secure connection
        server.login(smtp_username, smtp_password)
        server.sendmail(smtp_username, recipient_email, msg.as_string())
        server.quit()
        print("Email sent successfully.")
    except Exception as e:
        print("Failed to send email:", str(e))
@app.route("/")
def index():
    cpu_metric = psutil.cpu_percent()
    mem_metric = psutil.virtual_memory().percent
    Message = None

    if cpu_metric > 80 or mem_metric > 80:
        Message = "High CPU or Memory Detected, scale up!!!"
        send_email("Resource Alert", Message)

    return render_template("index.html", cpu_metric=cpu_metric, mem_metric=mem_metric, message=Message)
if __name__=='__main__':
    app.run(debug=True, host = '0.0.0.0')
