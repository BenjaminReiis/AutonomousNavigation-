class MotionController:


    def __init__(self):

        self.speed=0

        self.direction=0



    def move(self,target):


        self.speed=1.0


        self.direction=target



        return {


            "speed":

            self.speed,


            "direction":

            self.direction

        }



    def stop(self):


        self.speed=0


        return {


            "speed":0

        }
