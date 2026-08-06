#ifndef GPS_H
#define GPS_H

struct GPSData
{
    double latitude;
    double longitude;
    double altitude;
    float speed;
};

class GPS
{
public:
    void begin();
    void update();
    GPSData getData();

private:
    GPSData data;
};

#endif
