class Robot:


    def __init__(self, name):

        self.name = name

        self.status = "idle"

        self.battery = 100


        self.position = {

            "x":0,

            "y":0

        }



    def update_position(self,position):

        self.position = position



    def set_status(self,status):

        self.status=status



    def consume_battery(self,value):

        self.battery -= value


        if self.battery < 0:

            self.battery = 0



    def info(self):

        return {

            "name":self.name,

            "status":self.status,

            "battery":self.battery,

            "position":self.position

        }
