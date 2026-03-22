#ifndef UART_H
#define UART_H

#include <Arduino.h>

// Initialize UART communication
void uart_init(int baud_rate);

// Send a string message over UART
void uart_send(const char* message);

// Send structured JSON data over UART
void uart_send_json(float temperature, float humidity, float light);

#endif