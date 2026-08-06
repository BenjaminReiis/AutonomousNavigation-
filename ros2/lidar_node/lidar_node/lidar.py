import math
import random

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan


class LiDARNode(Node):

    def __init__(self):
        super().__init__("lidar_node")

        self.publisher = self.create_publisher(
            LaserScan,
            "/scan",
            10,
        )

        self.timer = self.create_timer(
            0.1,
            self.publish_scan,
        )

    def publish_scan(self):
        scan = LaserScan()

        scan.angle_min = 0.0
        scan.angle_max = 2.0 * math.pi
        scan.angle_increment = math.radians(1)

        scan.range_min = 0.15
        scan.range_max = 12.0

        total_points = 360

        scan.ranges = [
            random.uniform(0.5, 8.0)
            for _ in range(total_points)
        ]

        self.publisher.publish(scan)


def main(args=None):
    rclpy.init(args=args)

    node = LiDARNode()

    try:
        rclpy.spin(node)
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()
