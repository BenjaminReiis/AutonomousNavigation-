class SensorFusion:


    def __init__(self):

        self.weight_gps=0.6

        self.weight_imu=0.4



    def combine(
        self,
        gps,
        imu
    ):


        position={


            "latitude":

            gps["latitude"] *


            self.weight_gps,


            "longitude":

            gps["longitude"] *


            self.weight_gps,


            "orientation":

            imu["yaw"] *


            self.weight_imu

        }


        return position
