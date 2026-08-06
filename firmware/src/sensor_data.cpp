#include "sensor_data.h"


void SensorManager::begin()
{

    data.lidarDistance = 10.0;

    data.obstacle = false;

    data.cameraStatus = 1;

}



void SensorManager::update()
{

    data.lidarDistance -= 0.1;


    if(data.lidarDistance < 2.0)
    {

        data.obstacle = true;

    }
    else
    {

        data.obstacle = false;

    }


    if(data.lidarDistance < 0)
    {

        data.lidarDistance = 10.0;

    }

}



SensorData SensorManager::getData()
{

    return data;

}
