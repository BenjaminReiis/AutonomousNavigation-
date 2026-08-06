import cv2

import rclpy

from rclpy.node import Node

from sensor_msgs.msg import Image

from cv_bridge import CvBridge


class CameraNode(Node):

    def __init__(self):

        super().__init__("camera_node")

        self.publisher = self.create_publisher(
            Image,
            "/camera/image",
            10,
        )

        self.bridge = CvBridge()

        self.camera = cv2.VideoCapture(0)

        self.timer = self.create_timer(
            0.03,
            self.publish_frame,
        )

    def publish_frame(self):

        ok, frame = self.camera.read()

        if not ok:
            return

        msg = self.bridge.cv2_to_imgmsg(
            frame,
            encoding="bgr8",
        )

        self.publisher.publish(msg)

    def destroy_node(self):
        self.camera.release()
        super().destroy_node()


def main(args=None):

    rclpy.init(args=args)

    node = CameraNode()

    try:
        rclpy.spin(node)
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()
