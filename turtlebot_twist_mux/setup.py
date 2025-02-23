from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'turtlebot_twist_mux'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/turtlebot_twist_mux/launch', ['launch/twist_mux.launch.py']),
    ]+[(os.path.join('share', package_name, 'nodes'), glob('nodes/*.py'))],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='akm',
    maintainer_email='amit.kmaurya00@gmail.com',
    description='Custom twist_mux implementation for turtlebot',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'random_mover = turtlebot_twist_mux.random_mover:main',
            'twist_mux = turtlebot_twist_mux.twist_mux:main',
        ],
    },
)
