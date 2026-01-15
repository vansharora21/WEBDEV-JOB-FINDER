from utils.search import get_restaurants
from utils.filter import filter_no_website
from utils.email_sender import send_email
from utils.logger import log_contact
from utils.ai_email import generate_email   # AI part

from config import (
    EMAIL_ADDRESS,
    EMAIL_PASSWORD,
    LOCATION_COORDS
)

import time
import sys


def main(test_mode=False):
    print("🚀 Agent started...\n")
    
    if test_mode:
        print("🧪 TEST MODE - Emails will NOT be sent\n")

    # 2️⃣ Search for nearby restaurants using Overpass API (FREE - no API key needed!)
    print("🔍 Searching for restaurants using OpenStreetMap...")
    restaurants = get_restaurants(
        location=LOCATION_COORDS,
        radius=3000  # 3km radius
    )

    if not restaurants:
        print("❌ No restaurants found. Check your location coordinates.")
        return

    print(f"Found {len(restaurants)} restaurants\n")

    # 3️⃣ Filter restaurants WITHOUT websites
    print("🧹 Filtering restaurants without websites...")
    filtered_restaurants = filter_no_website(restaurants)

    print(f"{len(filtered_restaurants)} restaurants have NO website\n")

    # 4️⃣ Loop through filtered restaurants
    for restaurant in filtered_restaurants:
        name = restaurant.get("name")
        email = restaurant.get("email")  # From OSM data

        if not email:
            print(f"⚠️ No email found for {name}, skipping...")
            log_contact(name, "N/A", "email_not_found")
            continue

        print(f"✉️ Preparing email for {name}")

        # 5️⃣ Generate AI email
        email_body = generate_email(name)

        # 6️⃣ Send email (or test mode)
        if test_mode:
            print(f"📧 [TEST MODE] Would send email to {name}")
            print(f"   To: {email}")
            print(f"   Subject: Website idea for {name}")
            print(f"   Body: {email_body[:80]}...\n")
            log_contact(name, email, "test_mode")
            
        else:
            try:
                send_email(
                    sender=EMAIL_ADDRESS,
                    password=EMAIL_PASSWORD,
                    to=email,
                    subject=f"Website idea for {name}",
                    body=email_body
                )

                print(f"✅ Email sent to {name}")
                log_contact(name, email, "sent")

                # 7️⃣ Rate limit (VERY IMPORTANT)
                time.sleep(4)

            except Exception as e:
                print(f"❌ Failed to send email to {name}: {e}")
                log_contact(name, email, "failed")

    print("\n🎯 Agent finished successfully.")


if __name__ == "__main__":
    # Check for --test flag
    test_mode = "--test" in sys.argv
    main(test_mode=test_mode)
