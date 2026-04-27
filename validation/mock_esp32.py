#simulates esp32 output

import json
import random
import time

class MockESP32:
    def __init__(self): #construct the esp32
        self.initialized = True
    
    def generate_normal_reading(self):
        """Generate a valid sensor reading"""
        data = {
            "temp": round(random.uniform(20.0, 30.0), 2),
            "humidity": round(random.uniform(40.0, 70.0), 2),
            "light": round(random.uniform(100.0, 900.0), 2)
        }
        return json.dumps(data)
    
    def generate_out_of_range_reading(self):
        """Generate an out of range sensor reading"""
        data = {
            "temp": round(random.uniform(90.0, 150.0), 2), 
            "humidity": round(random.uniform(110.0, 200.0), 2),
            "light": round(random.uniform(100.0, 900.0), 2)
        }
        return json.dumps(data)
    
    def generate_error_reading(self):
        """Generate an error message"""
        errors = [ 
            "ERROR: OUT_OF_RANGE",
            "ERROR: TIMEOUT",
            "ERROR: NOT_INITIALIZED"
        ]
        return random.choice(errors)
    
    def generate_corrupted_reading(self): #garbage data not necessary out of range
        """Generate corrupted/invalid JSON"""
        return "invalid{json:data"

    def stream_data(self, count=10, interval=1.0): #stream only "good" values, the bad ones will apear in the tests
        """Stream sensor readings like a real ESP32 would"""
        for i in range(count):
            yield self.generate_normal_reading()
            time.sleep(interval)