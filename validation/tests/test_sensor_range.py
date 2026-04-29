#Chech if the values are in the correct range

from mock_esp32 import MockESP32  #import the class
import json

def test_temperature_range():

    mock_esp= MockESP32() #make new object
    data= json.loads (mock_esp.generate_normal_reading()) #read a data (normal) for initial checking
    temp=data["temp"]
    humidity=data["humidity"]
    light=data["light"]

    assert -40 <= temp<= 80, "Tempature out of normal range"
    assert 0 <= humidity <= 100, "Humidity out of normal range"
    assert 0 <= light <= 4095, "Light out of normal range"
    


