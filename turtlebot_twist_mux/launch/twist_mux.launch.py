from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='turtlebot_twist_mux',
            executable='twist_mux',
            name='twist_mux',
            output='screen'
        ),
        Node(
            package='turtlebot_twist_mux',
            executable='random_mover',
            name='random_mover',
            output='screen'
        ),
    ])
