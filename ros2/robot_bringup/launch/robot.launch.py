from launch import LaunchDescription

from launch_ros.actions import Node



def generate_launch_description():


    return LaunchDescription([


        Node(

            package="sensor_node",

            executable="sensor",

            name="sensor_node"

        ),



        Node(

            package="lidar_node",

            executable="lidar",

            name="lidar_node"

        ),



        Node(

            package="camera_node",

            executable="camera",

            name="camera_node"

        ),



        Node(

            package="navigation_node",

            executable="navigation",

            name="navigation_node"

        ),



        Node(

            package="control_node",

            executable="control",

            name="control_node"

        ),


    ])
