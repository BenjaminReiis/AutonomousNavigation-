import rclpy

from rclpy.node import Node

from std_msgs.msg import String


from camera import Camera

from yolo_detector import YOLODetector

from obstacle_detection import ObstacleDetection



class VisionNode(Node):


    def __init__(self):

        super().__init__(
            "vision_node"
        )


        self.publisher = self.create_publisher(

            String,

            "/detected_objects",

            10

        )


        self.obstacle_pub = self.create_publisher(

            String,

            "/obstacle_alert",

            10

        )


        self.camera = Camera()

        self.detector = YOLODetector()

        self.obstacle = ObstacleDetection()



        self.timer = self.create_timer(

            0.1,

            self.process

        )



    def process(self):


        frame = self.camera.read()


        if frame is None:

            return



        objects = self.detector.detect(

            frame

        )


        msg = String()


        msg.data = str(objects)


        self.publisher.publish(

            msg

        )



        alert = String()


        alert.data = str(

            self.obstacle.check(objects)

        )


        self.obstacle_pub.publish(

            alert

        )




def main(args=None):


    rclpy.init(args=args)


    node = VisionNode()


    rclpy.spin(node)


    node.destroy_node()


    rclpy.shutdown()



if __name__=="__main__":

    main()
