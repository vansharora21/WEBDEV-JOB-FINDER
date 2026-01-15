import csv
from datetime import datetime
import os

def log_contact(name, email, status):
    # Create data directory if it doesn't exist
    os.makedirs("data", exist_ok=True)
    
    # Create contacts.csv if it doesn't exist
    if not os.path.exists("data/contacts.csv"):
        with open("data/contacts.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["name", "email", "status", "timestamp"])
    
    # Append the contact
    with open("data/contacts.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([name, email, status, datetime.now()])
