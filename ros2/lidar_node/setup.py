from setuptools import setup

package_name = "lidar_node"

setup(
    name=package_name,
    version="1.0.0",
    packages=[package_name],
    install_requires=["setuptools"],
    zip_safe=True,
    maintainer="Robot",
    maintainer_email="robot@example.com",
    description="LiDAR Node",
    license="MIT",
    entry_points={
        "console_scripts": [
            "lidar=lidar_node.lidar:main",
        ],
    },
)
