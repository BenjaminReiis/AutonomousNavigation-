class CommandService:



    def __init__(self):

        self.status="ready"



    def execute(
        self,
        command
    ):


        if command=="START":


            self.status="running"



        elif command=="STOP":


            self.status="stopped"



        elif command=="EMERGENCY":


            self.status="emergency"



        return {


            "command":command,


            "status":self.status

        }
