import json
class JSONAgent:
    def process_json(self, json_data):
        required_fields = ["id", "amount", "date"]
        missing_fields = [field for field in required_fields if field not in json_data]

        if missing_fields:
            return f"Missing fields: {missing_fields}"
        return f"Processed JSON: {json.dumps(json_data, indent=2)}"