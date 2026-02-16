from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    publisher_node = Node(
        package='task02',
        executable='publisher',
        name='publisher',
        output='screen',
        parameters=[
            {
                'topic_name': '/chatter',
                'message': 'Hello, ROS2!',
                'text': 'Hello, ROS2!',
            }
        ],
    )

    return LaunchDescription([publisher_node])
