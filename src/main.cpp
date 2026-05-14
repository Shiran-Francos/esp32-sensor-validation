#include <Arduino.h>
#include "uart.h"
#include "sensor.h"

#define BAUD_RATE 115200
#define SAMPLE_INTERVAL_MS 2000

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
        char error_msg[50];
        snprintf(error_msg, sizeof(error_msg), 
            "ERROR: %s", sensor_get_error_str(data.error));
        uart_send(error_msg);
    }

    delay(SAMPLE_INTERVAL_MS);
}