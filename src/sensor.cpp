#include "sensor.h"

// Pin definitions
#define DHT_PIN 21
#define LDR_PIN 34 //input pin

// Range definitions
#define TEMP_MIN -40.0
#define TEMP_MAX 80.0
#define HUMIDITY_MIN 0.0
#define HUMIDITY_MAX 100.0
static bool initialized = false;

//declare the input pin
void sensor_init() {
    pinMode(LDR_PIN, INPUT);
    initialized = true; //set init to true
    Serial.println("Sensors initialized");
}

SensorData sensor_read() {
    SensorData data;
    
    // For now these are stubs - real sensor reading comes when hardware arrives
    data.temperature = 0.0;
    data.humidity = 0.0;
    data.light = 0.0;
    data.valid = false;
    if (!initialized) {   //error: init before read
        data.error = SENSOR_ERROR_NOT_INITIALIZED;
    }

    //UNTIL ESP ARRIVES!!!!

    data.temperature = 25.0;
    data.humidity = 60.0;
    data.light = 512.0;

    //error: out of range
    if (data.temperature < TEMP_MIN || data.temperature > TEMP_MAX) {
        data.error = SENSOR_ERROR_OUT_OF_RANGE;
        return data;
    }

    if (data.humidity < HUMIDITY_MIN || data.humidity > HUMIDITY_MAX) {
        data.error = SENSOR_ERROR_OUT_OF_RANGE;
        return data;
    }

    data.valid = true;
    data.error = SENSOR_OK;
    
    return data;
}

const char* sensor_get_error_str(SensorError error) {
    switch (error) {
        case SENSOR_OK:                    return "OK";
        case SENSOR_ERROR_TIMEOUT:         return "TIMEOUT";
        case SENSOR_ERROR_OUT_OF_RANGE:    return "OUT_OF_RANGE";
        case SENSOR_ERROR_NOT_INITIALIZED: return "NOT_INITIALIZED";
        default:                           return "UNKNOWN";
    }
}