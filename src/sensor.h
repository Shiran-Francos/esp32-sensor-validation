#ifndef SENSOR_H
#define SENSOR_H

#include <Arduino.h>

// Error codes
typedef enum {
    SENSOR_OK = 0,
    SENSOR_ERROR_TIMEOUT = 1, //sensor didnt respond in time
    SENSOR_ERROR_OUT_OF_RANGE = 2, //sensor returned value the is out of logic range
    SENSOR_ERROR_NOT_INITIALIZED = 3 //called read before init
} SensorError;

// Sensor data structure
struct SensorData {
    float temperature; //celsius
    float humidity; //percentage
    float light; //adc value 0-4095
    bool valid; //the reading was successful
    SensorError error; //what is the exact error
};

// Initialize sensors
void sensor_init();

// Read all sensors and return data
SensorData sensor_read();

// Get error description as string
const char* sensor_get_error_str(SensorError error);



#endif