from ultralytics import YOLO



class YOLODetector:


    def __init__(self):

        self.model = YOLO(
            "yolov8n.pt"
        )



    def detect(self, frame):

        results = self.model(frame)


        objects = []


        for result in results:

            for box in result.boxes:


                cls = int(
                    box.cls[0]
                )


                conf = float(
                    box.conf[0]
                )


                objects.append({

                    "class": cls,

                    "confidence": conf

                })


        return objects
