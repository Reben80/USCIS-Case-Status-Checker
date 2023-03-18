import requests
import warnings
import time
import smtplib
from email.mime.text import MIMEText
from bs4 import BeautifulSoup

# Disable the InsecureRequestWarning
warnings.filterwarnings("ignore", message="Unverified HTTPS request")

case_number = "YOUR_CASE_NUMBER"  # Replace with your own case number
url = "https://egov.uscis.gov/casestatus/mycasestatus.do"
payload = {"appReceiptNum": case_number}
headers = {"user-agent": "Mozilla/5.0"}

# Function to send email using Gmail
def send_email(message):
    # Set up email credentials and connection (replace with your own credentials)
    email = 'YOUR_EMAIL_ADDRESS'
    password = 'YOUR_EMAIL_PASSWORD'
    recipient = 'RECIPIENT_EMAIL_ADDRESS'
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email, password)

    # Create email message and send
    msg = MIMEText(message)
    msg['Subject'] = 'USCIS Case Status Update'
    msg['From'] = email
    msg['To'] = recipient
    server.sendmail(email, recipient, msg.as_string())
    server.quit()

# Loop to check USCIS case status every 24 hours
while True:
    # Send POST request to get case status
    response = requests.post(url, data=payload, headers=headers, verify=False)
    soup = BeautifulSoup(response.text, "html.parser")

    # Parse the response and get case status
    case_status = soup.find("div", {"class": "rows text-center"}).find("h1").text.strip()

    print("Your case status is:", case_status)
    send_email(f"Your case status is: {case_status}")  # Send email with case status
    time.sleep(86400)  # Sleep for 24 hours
