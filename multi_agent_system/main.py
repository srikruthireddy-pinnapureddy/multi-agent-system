from classifier_agent import ClassifierAgent
from json_agent import JSONAgent
from email_agent import EmailAgent
from memory_module import MemoryModule
import time

classifier = ClassifierAgent()
json_agent = JSONAgent()
email_agent = EmailAgent()
memory = MemoryModule()

def process_input(input_data):
    format, intent = classifier.classify(input_data)
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

    if format == "JSON":
        result = json_agent.process_json(input_data)
    elif format == "Email":
        result = email_agent.process_email(input_data)
    else:
        result = "Unsupported format"

    memory.log(str(input_data), format, timestamp, {"intent": intent, "result": result})
    return result

sample_json = {"id": 101, "amount": 500, "date": "2025-05-31"}
sample_email = "urgent RFQ request from abc@gmail.com"

print(process_input(sample_json))
print(process_input(sample_email))