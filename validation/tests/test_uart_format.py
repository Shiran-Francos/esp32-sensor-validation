#Check if the reading is valid JSON, has exactly the keys "temp", "humidity", "light" and that all the values are numbers
#Normal and Valid data is used
from mock_esp32 import MockESP32
import json
from jsonschema import validate, ValidationError

SCHEMA = {
        "type": "object",
        "properties": {
            "temp": {"type": "number"},
            "humidity": {"type": "number"},
            "light": {"type": "number"}
        },
        "required": ["temp", "humidity", "light"]
    }
def test_uart_format():

    mock_esp= MockESP32()
    data= json.loads (mock_esp.generate_normal_reading())

    try:
        validate(instance=data, schema=SCHEMA)
    except ValidationError as e:
       assert False, f"Json format wrong: {e.message}"  #the e.massege return the exact error 

#Check if an empty reading in caugth, raises an error massege if not
def test_empty_reading():

    mock_esp= MockESP32()
    data = json.loads(mock_esp.generate_empty_reading()) 

    try:
        validate(instance=data, schema=SCHEMA)
        assert False, "Empty reading! Should FAIL!"
    except ValidationError:
        pass      
    
def test_missing_key():
    mock_esp= MockESP32()
    data = json.loads(mock_esp.generate_missing_key()) 

    try:
        validate(instance=data, schema=SCHEMA)
        assert False, "Missing key (temp)! Should FAIL!"
    except ValidationError:
        pass      

def test_none_reading():
    mock_esp= MockESP32()
    data =mock_esp.generate_none_reading
    try:
        json.loads(data)
        assert False, "None reading! FAIL!"
    except (TypeError, json.JSONDecodeError):
        pass 

def test_string_key():
    mock_esp= MockESP32()
    data = json.loads(mock_esp.generate_string_key()) 

    try:
        validate(instance=data, schema=SCHEMA)
        assert False, "Temperatue is string instead of float! Should FAIL!"
    except ValidationError:
        pass 

