#include "uart.h"

void uart_init(int baud_rate) {
    Serial.begin(baud_rate);
    Serial.println("UART initialized");
}

void uart_send(const char* message) {
    Serial.println(message);
}

void uart_send_json(float temperature, float humidity, float light) {
    char buffer[100];
    snprintf(buffer, sizeof(buffer),
        "{\"temp\":%.2f,\"humidity\":%.2f,\"light\":%.2f}",
        temperature, humidity, light);
    Serial.println(buffer);
}