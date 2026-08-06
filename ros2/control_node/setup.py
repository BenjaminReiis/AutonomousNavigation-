from setuptools import setup

package_name = "control_node"

setup(
    name=package_name,
    version="1.0.0",
    packages=[package_name],
    install_requires=["setuptools"],
    zip_safe=True,
    maintainer="Robot",
    maintainer_email="robot@example.com",
    description="Control Node",
    license="MIT",
    entry_points={
        "console_scripts": [
            "control=control_node.control:main",
        ],
    },
)
