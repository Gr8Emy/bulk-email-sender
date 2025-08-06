import smtplib
import csv
from email.message import EmailMessage

# Your Gmail credentials
EMAIL = "your_email@gmail.com"
APP_PASSWORD = "your_app_password"

# Create email template
subject = "Upcoming Event Reminder"
body_template = """Hi {name},

This is a reminder about our upcoming event this weekend.
Looking forward to seeing you there!

Best regards,
Emmanuel
"""

# Load contacts from CSV
with open("contacts.csv", newline='') as file:
    reader = csv.DictReader(file)
    contacts = list(reader)

# Set up email server
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(EMAIL, APP_PASSWORD)

# Send email to each contact
for contact in contacts:
    msg = EmailMessage()
    msg["From"] = EMAIL
    msg["To"] = contact["email"]
    msg["Subject"] = subject
    msg.set_content(body_template.format(name=contact["name"]))

    server.send_message(msg)
    print(f"Email sent to {contact['name']}")

server.quit()
