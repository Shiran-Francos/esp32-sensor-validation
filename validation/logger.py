#logs data to CVS/JSON formats
#write down the info from each reading with a timestamp, the values, and whether it passed or failed 

import csv
import json
import os
from datetime import datetime

class Logger:
    def __init__(self, log_dir="logs"): #create a log file
        self.log_dir = log_dir
        os.makedirs(log_dir, exist_ok=True)
        self.timestamp = datetime.now().strftime("%Y%m%d_%H%M%S") #make sure it has a unique name
        self.csv_file = f"{log_dir}/log_{self.timestamp}.csv"
        self.json_file = f"{log_dir}/log_{self.timestamp}.json"
        self.entries = [] #empty list that will store all logs
        self._init_csv()

    def _init_csv(self): #each cvs file has headers : "timestamp", "temperature", "humidity", "light", "status", "error"
        with open(self.csv_file, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["timestamp", "temperature", 
                           "humidity", "light", "status", "error"])

    def log(self, data, status, error=""): #every tine we have a reading we will call the log func 
        """Log a single entry"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = {
            "timestamp": timestamp,
            "temperature": data.get("temp", "N/A"),
            "humidity": data.get("humidity", "N/A"),
            "light": data.get("light", "N/A"),
            "status": status,
            "error": error
        }
        self.entries.append(entry)
        self._write_csv(entry)
        self._write_json()

    def _write_csv(self, entry):
        """Append entry to CSV file"""
        with open(self.csv_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(entry.values())

    def _write_json(self):
        """Write all entries to JSON file"""
        with open(self.json_file, 'w') as f:
            json.dump(self.entries, f, indent=2)

    def get_summary(self):
        """Return a summary of all logged entries"""
        total = len(self.entries)
        passed = sum(1 for e in self.entries if e["status"] == "PASS")
        failed = total - passed
        return {
            "total": total,
            "passed": passed,
            "failed": failed,
            "pass_rate": f"{(passed/total*100):.1f}%" if total > 0 else "N/A"
        }