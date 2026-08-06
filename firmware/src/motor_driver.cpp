#include "motor_driver.h"

#include "config.h"

#include <Arduino.h>

void MotorDriver::begin()
{
    pinMode(PWM_LEFT,OUTPUT);
    pinMode(PWM_RIGHT,OUTPUT);

    pinMode(DIR_LEFT,OUTPUT);
    pinMode(DIR_RIGHT,OUTPUT);
}

void MotorDriver::setSpeed(int left,int right)
{
    digitalWrite(DIR_LEFT,left>=0);
    digitalWrite(DIR_RIGHT,right>=0);

    analogWrite(PWM_LEFT,abs(left));
    analogWrite(PWM_RIGHT,abs(right));
}

void MotorDriver::stop()
{
    analogWrite(PWM_LEFT,0);
    analogWrite(PWM_RIGHT,0);
}
