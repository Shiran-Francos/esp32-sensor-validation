#ifndef SENSOR_H
#define SENSOR_H

#include <Arduino.h>

// Sensor data structure
struct SensorData {
    float temperature; //celsius
    float humidity; //percentage
    float light; //adc value 0-4095
    bool valid; //the reading was successful
};

// Initialize sensors
void sensor_init();

// Read all sensors and return data
SensorData sensor_read();

#endif