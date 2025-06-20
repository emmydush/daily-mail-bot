import smtplib
from email.message import EmailMessage
from datetime import datetime
import schedule
import time
import os

EMAIL_ADDRESS = "emmychris915@gmail.com"       
EMAIL_PASSWORD = "mjzh konc tcpj htdp"       

recipients = [
    "kubwimanatheophile02@gmail.com",
    "muhayimanaemilien@gmail.com",
    "basesayosejmv@gmail.com",
    "aishimwe394@gmail.com",
]

def send_payment_reminders():
    for recipient in recipients:
        msg = EmailMessage()
        msg['Subject'] = "Payment Reminder"
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = recipient

        msg.set_content(f"""
        Dear Customer,

        This is a friendly reminder that your payment is due on {datetime.now().strftime('%d %B %Y')}.

        Kindly make your payment to avoid any late fees.

        Thank you!
        """)

        try:
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                smtp.send_message(msg)
                print(f" Email sent to {recipient}")
        except Exception as e:
            print(f" Failed to send to {recipient}: {e}")

if __name__ == "__main__":
    send_payment_reminders()  

schedule.every().day.at("08:00").do(send_payment_reminders)

print("🔄 Scheduler running... Will send to 10 people daily at 08:00 AM")
while True:
    schedule.run_pending()
    time.sleep(60)   
