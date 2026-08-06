#ifndef IMU_H
#define IMU_H

struct IMUData
{
    float roll;
    float pitch;
    float yaw;

    float ax;
    float ay;
    float az;

    float gx;
    float gy;
    float gz;
};

class IMU
{
public:

    void begin();

    void update();

    IMUData getData();

private:

    IMUData data;
};

#endif
