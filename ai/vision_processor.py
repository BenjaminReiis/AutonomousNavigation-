import cv2


class VisionProcessor:


    def __init__(self):

        self.camera_active=True



    def process(self, frame):


        image=cv2.resize(

            frame,

            (640,480)

        )


        return image



    def analyze_brightness(self,frame):


        gray=cv2.cvtColor(

            frame,

            cv2.COLOR_BGR2GRAY

        )


        brightness=gray.mean()


        return brightness
