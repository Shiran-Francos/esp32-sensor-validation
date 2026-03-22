#include "sensor.h"

// Pin definitions
#define DHT_PIN 21
#define LDR_PIN 34

void sensor_init() {
    pinMode(LDR_PIN, INPUT);
    Serial.println("Sensors initialized");
}

SensorData sensor_read() {
    SensorData data;
    
    // For now these are stubs - real sensor reading comes when hardware arrives
    data.temperature = 0.0;
    data.humidity = 0.0;
    data.light = 0.0;
    data.valid = false;
    
    return data;
}