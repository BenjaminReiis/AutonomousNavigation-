#include <Arduino.h>

#include "motor_driver.h"

MotorDriver motor;

void setup()
{
    Serial.begin(115200);

    motor.begin();

    Serial.println("Robot Started");
}

void loop()
{
    motor.setSpeed(150,150);

    delay(3000);

    motor.stop();

    delay(1000);
}
