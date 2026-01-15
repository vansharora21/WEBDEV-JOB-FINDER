import re
import requests

EMAIL_REGEX = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

def find_email(text):
    matches = re.findall(EMAIL_REGEX, text)
    for email in matches:
        if not email.endswith(("gmail.com", "yahoo.com")):
            return email
    return None


