import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class Task02(Node):
    def __init__(self):
        super().__init__('publisher')
        self.get_logger().info("Receiver node has been started")

        self.declare_parameters(
            namespace='',
            parameters=[
                ('topic_name', None),
                ('message', 'Hello, ROS2!')
            ])

        self._topic = self.get_parameter('topic_name').get_parameter_value().string_value
        self._text = self.get_parameter('text').get_parameter_value().string_value

        self._pub = self.create_publisher(String, self._topic, 10)
        self._timer = self.create_timer(0.5, self._on_timer)

    def _on_timer(self):
        msg = String()
        msg.data = self._text
        self._pub.publish(msg)


def main():
    rclpy.init()
    node = Task02()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
