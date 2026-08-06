import random
import time


class Lidar:


    def __init__(self):

        self.range = 100



    def scan(self):

        distances = []


        for i in range(360):

            distance = random.uniform(
                0.5,
                self.range
            )

            distances.append(distance)


        return {

            "points": distances,

            "timestamp": time.time()

        }
