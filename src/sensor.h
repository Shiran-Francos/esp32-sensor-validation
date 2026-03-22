#ifndef SENSOR_H
#define SENSOR_H

#include <Arduino.h>

// Sensor data structure
struct SensorData {
    float temperature;
    float humidity;
    float light;
    bool valid;
};

// Initialize sensors
void sensor_init();

// Read all sensors and return data
SensorData sensor_read();

#endif