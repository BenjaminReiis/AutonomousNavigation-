#ifndef SENSOR_DATA_H
#define SENSOR_DATA_H


struct SensorData
{

    float lidarDistance;

    bool obstacle;

    int cameraStatus;

};


class SensorManager
{

public:

    void begin();

    void update();

    SensorData getData();


private:

    SensorData data;

};


#endif
