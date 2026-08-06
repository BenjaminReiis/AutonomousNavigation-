from ultralytics import YOLO


class ObjectDetector:


    def __init__(self):

        # Modelo inicial YOLO
        # Pode ser substituído por modelo treinado

        self.model = YOLO("yolov8n.pt")



    def detect(self, image):


        results = self.model(
            image
        )


        objects=[]


        for result in results:


            for box in result.boxes:


                objects.append({

                    "class":
                    int(box.cls[0]),


                    "confidence":
                    float(box.conf[0]),


                    "box":
                    box.xyxy.tolist()

                })


        return objects
