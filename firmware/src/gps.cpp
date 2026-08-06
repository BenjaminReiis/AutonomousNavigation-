#include "gps.h"

void GPS::begin()
{
    data.latitude = -23.550520;
    data.longitude = -46.633308;
    data.altitude = 760.0;
    data.speed = 0.0;
}

void GPS::update()
{
    data.latitude += 0.000001;
    data.longitude += 0.000001;
}

GPSData GPS::getData()
{
    return data;
}
