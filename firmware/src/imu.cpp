#include "imu.h"

void IMU::begin()
{
    data.roll = 0;
    data.pitch = 0;
    data.yaw = 0;

    data.ax = 0;
    data.ay = 0;
    data.az = 9.81;

    data.gx = 0;
    data.gy = 0;
    data.gz = 0;
}

void IMU::update()
{
    data.yaw += 0.05f;

    if(data.yaw > 360.0f)
    {
        data.yaw = 0.0f;
    }
}

IMUData IMU::getData()
{
    return data;
}
