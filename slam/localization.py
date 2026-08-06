class Localization:


    def __init__(self):

        self.position={

            "x":0,

            "y":0,

            "angle":0

        }



    def update(
        self,
        imu,
        gps
    ):


        self.position["angle"]=imu["yaw"]


        self.position["x"]=gps["latitude"]

        self.position["y"]=gps["longitude"]



        return self.position
