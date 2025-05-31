import sqlite3
import json
class MemoryModule:
    def __init__(self):
        self.conn = sqlite3.connect("memory.db")
        self.create_table()

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS memory (
            id INTEGER PRIMARY KEY,
            source TEXT,
            type TEXT,
            timestamp TEXT,
            extracted_values TEXT
        )
        """
        self.conn.execute(query)
        self.conn.commit()

    def log(self, source, type, timestamp, values):
        query = "INSERT INTO memory (source, type, timestamp, extracted_values) VALUES (?, ?, ?, ?)"
        self.conn.execute(query, (source, type, timestamp, json.dumps(values)))
        self.conn.commit()