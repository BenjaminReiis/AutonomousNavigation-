class RobotDecision:


    def decide(

        self,

        obstacle,

        battery

    ):


        if battery < 20:

            return "RETURN_HOME"



        if obstacle:

            return "AVOID"



        return "MOVE"
