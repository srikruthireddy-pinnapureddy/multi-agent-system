# Multi-Agent AI System

## **Overview**
This project implements a multi-agent AI system that processes PDF, JSON, and Email inputs, classifies them, and routes them to the correct processing agent while maintaining shared context.

## **Agents Included**
- **Classifier Agent**: Determines input format and intent.
- **JSON Agent**: Extracts relevant data and validates schema.
- **Email Agent**: Extracts sender info, urgency, and intent.

## **Shared Memory Module**
The system maintains memory using SQLite, storing:
- Source, type, timestamp
- Extracted fields
- Thread context for chaining responses

## **Installation & Setup**
### **Prerequisites**
- Python 3.x
- Dependencies from `requirements.txt`

### **Installation**
```bash
cd multi_agent_system
pip install -r requirements.txt
