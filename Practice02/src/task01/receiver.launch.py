from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    receiver_node = Node(
        package='task01',
        executable='receiver',
        name='receiver',
        output='screen',
        parameters=[],
        remappings=[],
    )

    return LaunchDescription([receiver_node])
