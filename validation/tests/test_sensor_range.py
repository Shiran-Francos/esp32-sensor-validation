from mock_esp32 import MockESP32
import json

def test_temperature_range():
    mock_esp= MockESP32()
    data= json.loads (mock_esp.generate_normal_reading())
    temp=data["temp"]
    humidity=data["humidity"]
    light=data["light"]

    assert -40 <= temp<= 80, "Tempature out of normal range"
    assert 0 <= humidity <= 100, "humidity out of normal range"
    assert 0 <= light <= 4095, "light out of normal range"
    


