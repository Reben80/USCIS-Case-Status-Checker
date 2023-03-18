# USCIS Case Status Checker

This Python script checks the status of a USCIS case and sends an email notification with the current case status. It runs in a loop and checks the case status every 24 hours.

## Prerequisites

* Python 3
* BeautifulSoup 4
* requests

You can install the required packages using pip:

```bash
pip install beautifulsoup4 requests
```
## Usage

1.  Replace YOUR_CASE_NUMBER
 2. YOUR_EMAIL_ADDRESS
 3. YOUR_EMAIL_PASSWORD, and
 4. RECIPIENT_EMAIL_ADDRESS in the script with your own information.
5. Save the script as case_status_checker.py.
6. Run the script using the following command:
```python case_status_checker.py```

The script will continuously run and check your case status every 24 hours, sending an email notification with the current case status.

## Gmail Users
If you are using Gmail, make sure to follow these steps:

1. Enable 2-Step Verification (2FA) for your Gmail account. You can find instructions on how to do this [here](https://support.google.com/accounts/answer/185839?hl=en).
2. Create an App Password for your Gmail account. This will be used in the script instead of your regular Gmail password. Instructions for creating an App Password can be found [here](https://support.google.com/accounts/answer/185833?hl=en).


## Disclaimer

Please be aware that this script uses your email address and password to send the notification emails. It is recommended to use environment variables or a configuration file to store sensitive information securely.

Also, note that the script ignores HTTPS verification warnings.
