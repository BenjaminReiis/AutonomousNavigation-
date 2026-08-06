#include "encoder.h"

#include "config.h"

#include <Arduino.h>

long leftTicks=0;

long rightTicks=0;

void Encoder::begin()
{

    pinMode(
        ENCODER_LEFT,
        INPUT
    );

    pinMode(
        ENCODER_RIGHT,
        INPUT
    );

}

long Encoder::left()
{
    return leftTicks;
}

long Encoder::right()
{
    return rightTicks;
}
