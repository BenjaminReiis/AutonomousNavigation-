import cv2


class Camera:

    def __init__(self, index=0):

        self.camera = cv2.VideoCapture(index)


    def read(self):

        status, frame = self.camera.read()

        if status:

            return frame

        return None


    def release(self):

        self.camera.release()
