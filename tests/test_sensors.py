from sensors.sensor_manager import SensorManager



def test_sensor_system():


    sensors = SensorManager()


    data = sensors.collect_data()


    assert "gps" in data

    assert "imu" in data

    assert "lidar" in data

    assert "camera" in data
