import time


class TelemetryManager:


    def __init__(self):

        self.data=[]



    def record(self,robot):


        info={


            "time":

            time.time(),


            "robot":

            robot.info()


        }


        self.data.append(info)


        return info



    def history(self):

        return self.data
