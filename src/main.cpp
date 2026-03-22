#include <Arduino.h>
#include "uart.h"
#include "sensor.h"

#define BAUD_RATE 115200
#define SAMPLE_INTERVAL_MS 1000

void setup() {
    uart_init(BAUD_RATE);
    sensor_init();
    uart_send("System initialized");
}

void loop() {
    SensorData data = sensor_read();
    
    if (data.valid) {
        uart_send_json(data.temperature, data.humidity, data.light);
    } else {
        uart_send("ERROR: Invalid sensor reading");
    }
    
    delay(SAMPLE_INTERVAL_MS);
}