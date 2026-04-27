#Check if the reading is valid JSON, has exactly the keys "temp", "humidity", "light" and that all the values are numbers

from mock_esp32 import MockESP32
import json
from jsonschema import validate, ValidationError

def test_uart_format():

    mock_esp= MockESP32()
   
    schema = {
        "type": "object",
        "properties": {
            "temp": {"type": "number"},
            "humidity": {"type": "number"},
            "light": {"type": "number"}
        },
        "required": ["temp", "humidity", "light"]
    }

    data= json.loads (mock_esp.generate_normal_reading())

    try:
        validate(instance=data, schema=schema)
    except ValidationError as e:
       assert False, f"Json format wrong": {e.message}  #the e.massege return the exact error 