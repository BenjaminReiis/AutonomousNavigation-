from setuptools import setup
from glob import glob
import os


package_name = "robot_bringup"


setup(

    name=package_name,

    version="1.0.0",

    packages=[package_name],

    data_files=[

        (

            "share/ament_index/resource_index/packages",

            [

                "resource/" + package_name

            ],

        ),


        (

            "share/" + package_name,

            glob("launch/*.py")

        ),

    ],


    install_requires=[
        "setuptools"
    ],


    zip_safe=True,


    maintainer="Robot",

    maintainer_email="robot@example.com",


    description="Robot Bringup",

    license="MIT",

)
