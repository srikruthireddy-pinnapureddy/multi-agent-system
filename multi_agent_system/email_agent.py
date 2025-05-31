import re

class EmailAgent:
    def process_email(self, email_text):
        sender = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+", email_text)
        urgency = "High" if "urgent" in email_text.lower() else "Normal"
        return f"Sender: {sender}, Urgency: {urgency}, Processed email."