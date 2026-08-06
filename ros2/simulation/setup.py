from setuptools import setup

from glob import glob


package_name="simulation"


setup(

name=package_name,

version="1.0.0",

packages=[package_name],


data_files=[


(
"share/ament_index/resource_index/packages",

[
"resource/"+package_name
]

),



(
"share/"+package_name,

glob("launch/*.py")

),



(
"share/"+package_name+"/worlds",

glob("worlds/*.world")

)


],


install_requires=[

"setuptools"

],


zip_safe=True,


description="Gazebo Simulation",

license="MIT"

)
