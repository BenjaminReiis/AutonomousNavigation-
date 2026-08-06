from camera import Camera

from yolo_detector import YOLODetector

from obstacle_detection import ObstacleDetection



camera = Camera()

detector = YOLODetector()

obstacle = ObstacleDetection()



while True:


    frame = camera.read()


    if frame is None:

        continue



    objects = detector.detect(
        frame
    )


    danger = obstacle.check(
        objects
    )


    print(
        "Objetos:",
        objects
    )


    print(
        "Obstáculo:",
        danger
    )
