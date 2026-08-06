class DecisionEngine:


    def __init__(self):

        self.mode="autonomous"



    def decide(
        self,
        objects,
        obstacles
    ):


        dangerous_objects=[]


        for obj in objects:


            if obj["confidence"] > 0.6:


                dangerous_objects.append(obj)



        if len(dangerous_objects)>0:


            return {


                "action":
                "avoid",


                "reason":
                "object_detected"


            }



        if obstacles:


            return {


                "action":
                "stop",


                "reason":
                "obstacle"


            }



        return {


            "action":
            "continue",


            "reason":
            "clear_path"

        }
