class MissionManager:


    def __init__(self):

        self.current_mission=None



    def create_mission(
        self,
        start,
        destination
    ):


        self.current_mission={


            "start":start,


            "destination":destination,


            "status":"created"


        }


        return self.current_mission



    def start(self):


        if self.current_mission:


            self.current_mission["status"]="running"



        return self.current_mission



    def finish(self):


        if self.current_mission:


            self.current_mission["status"]="completed"



        return self.current_mission
