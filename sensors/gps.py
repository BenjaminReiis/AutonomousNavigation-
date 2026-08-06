import random
import time


class GPS:

    def __init__(self):

        self.latitude = 0.0
        self.longitude = 0.0


    def read(self):

        self.latitude += random.uniform(-0.0001, 0.0001)

        self.longitude += random.uniform(-0.0001, 0.0001)


        return {

            "latitude": self.latitude,

            "longitude": self.longitude,

            "timestamp": time.time()

        }
