import os


from launch import LaunchDescription

from launch.actions import IncludeLaunchDescription

from launch.launch_description_sources import PythonLaunchDescriptionSource


from launch_ros.actions import Node


from ament_index_python.packages import get_package_share_directory



def generate_launch_description():


    gazebo_path = os.path.join(

        get_package_share_directory(
            "gazebo_ros"
        ),

        "launch",

        "gazebo.launch.py"

    )



    world_path = os.path.join(

        get_package_share_directory(
            "simulation"
        ),

        "worlds",

        "test_world.world"

    )



    robot_description_path = os.path.join(

        get_package_share_directory(
            "robot_description"
        ),

        "urdf",

        "autonomous_robot.urdf"

    )



    with open(robot_description_path,"r") as file:

        robot_description=file.read()



    return LaunchDescription([



        IncludeLaunchDescription(

            PythonLaunchDescriptionSource(

                gazebo_path

            ),

            launch_arguments={

                "world":

                world_path

            }.items()

        ),



        Node(

            package="robot_state_publisher",

            executable="robot_state_publisher",

            parameters=[

                {

                "robot_description":

                robot_description

                }

            ]

        ),




        Node(

            package="gazebo_ros",

            executable="spawn_entity.py",

            arguments=[

                "-entity",

                "autonomous_robot",

                "-topic",

                "robot_description"

            ],

            output="screen"

        )


    ])
