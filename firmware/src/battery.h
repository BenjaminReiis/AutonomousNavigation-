#ifndef BATTERY_H
#define BATTERY_H

class Battery
{
public:
    void begin();
    float voltage();
    int percentage();
};

#endif
