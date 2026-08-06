import json



class VisionPublisher:


    def create_message(
        self,
        objects
    ):


        data = {


            "objects": objects,


            "count": len(objects)


        }


        return json.dumps(data)
