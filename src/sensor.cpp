#include "sensor.h"
#include <DHT.h>

#define DHT_PIN 4
#define DHT_TYPE DHT22
#define LDR_PIN 34

#define TEMP_MIN -40.0
#define TEMP_MAX 80.0
#define HUMIDITY_MIN 0.0
#define HUMIDITY_MAX 100.0

static bool initialized = false;
static DHT dht(DHT_PIN, DHT_TYPE);

void sensor_init() {
    pinMode(LDR_PIN, INPUT);
    dht.begin();
    initialized = true;
    Serial.println("Sensors initialized");
}

SensorData sensor_read() {
    SensorData data;
    data.valid = false;
    data.temperature = 0.0;
    data.humidity = 0.0;
    data.light = 0.0;

    if (!initialized) {
        data.error = SENSOR_ERROR_NOT_INITIALIZED;
        return data;
    }

    data.temperature = dht.readTemperature();
    data.humidity = dht.readHumidity();
    data.light = 0.0;  // LDR not connected yet

    if (isnan(data.temperature) || isnan(data.humidity)) {
        data.error = SENSOR_ERROR_TIMEOUT;
        return data;
    }

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