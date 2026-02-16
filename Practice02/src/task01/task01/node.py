import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class SimpleNode(Node):
    def __init__(self):
        super(SimpleNode, self).__init__('receiver')
        self.get_logger().info("Receiver node has been started")
        self.message_topic = '/spgc/sender'
        self.subscription = self.create_subscription(
            String,
            self.message_topic,
            self.listener_callback,
            10
        )
        self.get_logger().info("Subscription to topic has been created")

    def listener_callback(self, msg):
        self.get_logger().info(f"Received message: {msg.data}")


def main():
    rclpy.init()
    node = SimpleNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
