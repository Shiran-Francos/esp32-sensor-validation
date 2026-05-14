from serial_reader import SerialReader
import json
import pytest
from jsonschema import validate, ValidationError
import time

SCHEMA = {
        "type": "object",
        "properties": {
            "temp": {"type": "number"},
            "humidity": {"type": "number"},
            "light": {"type": "number"}
        },
        "required": ["temp", "humidity", "light"]
    }

def test_hardware_values():

    reader=SerialReader(115200,'COM3')
    data=None
    for i in range(20):  # try up to 10 lines
        line = reader.read_line()
        if line and line.startswith("{"): #a line with data was found
            data = json.loads(line)
            break
    reader.close()
    time.sleep(1)
    assert data is not None, "No valid JSON received!"
    temp=data["temp"]
    humidity=data["humidity"]

    #temp and humidity are floats and not strings
    assert isinstance(temp,float), "Tempature is a string, should be float!"
    assert isinstance(humidity,float), "Humidity is a string, should be float!"

    #temp and humidity in the large range 
    assert -40<=temp<=80, "Tempature out of range!"
    assert 0 <= humidity <= 100, "Humidity out of normal range!"

    #temp and humidity in realistic range
    assert 15<=temp<=40, "Tempature out of range!"
    assert 40 <= humidity <= 90, "Humidity out of normal range!"
    
    #temp and humidity are real sensor readings and not the stubs
    assert temp != 25.0, "Tempature is stub! Not real reading!"
    assert humidity != 60.0, "humidity is stub! Not real reading!"

def test_hardware_consecutive_readings():

    reader=SerialReader(115200,'COM3')
    data=None
    data_list = []
    count=0
    for i in range(20):  # try up to 20 lines
        line = reader.read_line()
        if line and line.startswith("{"): #a line with data was found
            count=count+1
            data = json.loads(line)
            data_list.append({"temp": data["temp"], "humidity": data["humidity"]})
            time.sleep(2)
            if count==4:
                break
    reader.close()
    time.sleep(2)
    assert data is not None, "No valid JSON received!"
    assert count==4, "Did not receive 3 valid readings!"
    temps = [d["temp"] for d in data_list]
    humid=[h["humidity"] for h in data_list]
    assert len(set(temps)) > 1, "All readings are the same, Error accured with the sensor"
    assert len(set(humid)) > 1, "All readings are the same, Error accured with the sensor"

def test_hardware_json_format():
    reader=SerialReader(115200,'COM3')
    data=None
    for i in range(20):
        line = reader.read_line()
        if line and line.startswith("{"): #a line with data was found
            data = json.loads(line)
            break
    reader.close()
    time.sleep(1)
    assert data is not None, "No valid JSON received!"
    try:
        validate(instance=data, schema=SCHEMA)
    except ValidationError as e:
       assert False, f"Json format wrong: {e.message}"  #the e.massege return the exact error 

def test_hardware_timing():
    reader=SerialReader(115200,'COM3')
    data=None
    count=0
    for i in range(100):
        line = reader.read_line()
        if line and line.startswith("{"): #a line with data was found
            if (count==0):
                start_time=time.time()
            count=count+1
            data = json.loads(line)
            if (count==20):
                end_time=time.time()
                break
    reader.close()
    assert data is not None, "No valid JSON received!"
    assert 35<end_time-start_time <55, "Problem with the sampling time, no 2 seconds between readings!"