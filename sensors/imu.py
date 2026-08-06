import random
import time


class IMU:

    def __init__(self):

        self.orientation = 0


    def read(self):

        self.orientation += random.uniform(-2,2)


        return {

            "roll": random.uniform(-1,1),

            "pitch": random.uniform(-1,1),

            "yaw": self.orientation,

            "timestamp": time.time()

        }
