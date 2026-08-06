from sensors.gps import GPS
from sensors.imu import IMU
from sensors.lidar import Lidar
from sensors.camera import Camera



class SensorManager:


    def __init__(self):

        self.gps = GPS()

        self.imu = IMU()

        self.lidar = Lidar()

        self.camera = Camera()



    def collect_data(self):


        return {


            "gps":

            self.gps.read(),


            "imu":

            self.imu.read(),


            "lidar":

            self.lidar.scan(),


            "camera":

            self.camera.capture()


        }
