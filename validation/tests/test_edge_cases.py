
from mock_esp32 import MockESP32  #import the class
import json

mock_esp=MockESP32()

def test_out_of_range():

    data=json.loads (mock_esp.generate_out_of_range_reading())
    temp=data["temp"]
    humidity=data["humidity"]
    assert temp>150 or temp<90, "Tempature should be out of normal range!"
    assert humidity<200 or humidity>110, "Humidity should be out of normal range!"

def test_error_reding():

    data= (mock_esp.generate_error_reading())
    assert data.startswith("ERROR:"), f"Expected ERROR message, the error is: {data}"

def test_corrupted_reading():
    data = mock_esp.generate_corrupted_reading()
    try:
        json.loads(data)
        assert False, "Expected an exeption message!"
    except json.JSONDecodeError:
        pass 