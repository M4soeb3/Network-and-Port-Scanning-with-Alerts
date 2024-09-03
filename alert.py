import smtplib
from email.mime.text import MIMEText

def send_email_alert(subject, body):
    # Email configuration
    smtp_server = 'smtp.example.com'
    smtp_port = 587
    smtp_user = 'your_email@example.com'
    smtp_password = 'your_password'
    to_email = 'alert_recipient@example.com'

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = smtp_user
    msg['To'] = to_email

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_user, smtp_password)
        server.sendmail(smtp_user, to_email, msg.as_string())

def check_for_alerts(devices):
    for device in devices:
        open_ports = scan_ports(device['ip'], range(1, 1025))
        if open_ports:
            alert_body = f"Device {device['ip']} has open ports: {', '.join(map(str, open_ports))}"
            print(f"Alert: {alert_body}")
            send_email_alert("Open Ports Alert", alert_body)

# Define IP range
ip_range = '192.168.122.1/24'
devices = scan_network(ip_range)
print_results(devices)
check_for_alerts(devices)

