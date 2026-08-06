import random

import rclpy

from rclpy.node import Node

from sensor_msgs.msg import LaserScan

from sensor_msgs.msg import Imu

from sensor_msgs.msg import NavSatFix


class SensorNode(Node):

    def __init__(self):
        super().__init__("sensor_node")

        self.lidar_pub = self.create_publisher(
            LaserScan,
            "/scan",
            10,
        )

        self.gps_pub = self.create_publisher(
            NavSatFix,
            "/gps",
            10,
        )

        self.imu_pub = self.create_publisher(
            Imu,
            "/imu",
            10,
        )

        self.timer = self.create_timer(
            0.1,
            self.publish_data,
        )

    def publish_data(self):
        gps = NavSatFix()
        gps.latitude = -23.55052 + random.uniform(-0.0001, 0.0001)
        gps.longitude = -46.63330 + random.uniform(-0.0001, 0.0001)

        imu = Imu()
        imu.orientation.w = 1.0

        lidar = LaserScan()
        lidar.angle_min = 0.0
        lidar.angle_max = 6.28
        lidar.angle_increment = 0.01
        lidar.range_min = 0.10
        lidar.range_max = 20.0
        lidar.ranges = [5.0] * 628

        self.gps_pub.publish(gps)
        self.imu_pub.publish(imu)
        self.lidar_pub.publish(lidar)


def main(args=None):
    rclpy.init(args=args)

    node = SensorNode()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == "__main__":
    main()
