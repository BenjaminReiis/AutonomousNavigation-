class ObstacleAvoidance:


    def __init__(self):

        self.safe_distance = 2.0



    def check(self,lidar_data):


        obstacles=[]


        for index,distance in enumerate(lidar_data):


            if distance < self.safe_distance:

                obstacles.append(index)



        return {


            "blocked":

            len(obstacles)>0,


            "positions":

            obstacles

        }
