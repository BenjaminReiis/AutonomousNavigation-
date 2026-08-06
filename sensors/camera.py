import time


class Camera:


    def __init__(self):

        self.running = False



    def start(self):

        self.running = True



    def capture(self):

        if not self.running:

            self.start()


        return {

            "frame":

            "camera_image_data",

            "timestamp":

            time.time()

        }
