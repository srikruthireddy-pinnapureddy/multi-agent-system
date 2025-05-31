import json
import re

class ClassifierAgent:
    def classify(self, input_data):
        if isinstance(input_data, dict):
            return "JSON", self.detect_intent(input_data)
        elif isinstance(input_data, str):
            if "@gmail.com" in input_data:
                return "Email", self.detect_intent(input_data)
            else:
                return "Text", self.detect_intent(input_data)
        else:
            return "Unknown", None

    def detect_intent(self, data):
        if "invoice" in str(data).lower():
            return "Invoice"
        elif "rfq" in str(data).lower():
            return "RFQ"
        elif "complaint" in str(data).lower():
            return "Complaint"
        else:
            return "Unknown"
