#include <Arduino.h>

// put function declarations here:


void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  Serial.println("ESP32 is alive!");
}

void loop() {
  // put your main code here, to run repeatedly:
    Serial.println("Running...");
    delay(1000);
}

// put function definitions here:
