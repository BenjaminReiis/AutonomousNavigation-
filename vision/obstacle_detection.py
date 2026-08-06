class ObstacleDetection:


    def check(
        self,
        objects
    ):

        dangerous = []


        for obj in objects:


            if obj["confidence"] > 0.6:

                dangerous.append(obj)



        return len(dangerous) > 0
