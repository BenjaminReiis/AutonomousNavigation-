from slam.map import OccupancyMap

from slam.localization import Localization

from slam.sensor_fusion import SensorFusion



class SLAMEngine:


    def __init__(self):


        self.map = OccupancyMap(

            100,

            100

        )


        self.localization = Localization()


        self.fusion = SensorFusion()



    def process(
        self,
        gps,
        imu,
        lidar
    ):


        position = self.localization.update(

            imu,

            gps

        )


        for index,distance in enumerate(lidar):


            if distance < 5:


                x=index % 100

                y=index // 100


                self.map.update(

                    x,

                    y,

                    True

                )



        return {


            "position":

            position,


            "map":

            self.map.get_map()

        }
