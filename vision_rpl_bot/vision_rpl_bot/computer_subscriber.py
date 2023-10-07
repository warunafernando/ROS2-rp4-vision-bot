import rclpy
from rclpy.node import Node

from std_msgs.msg import Int16


class ComputerSubscriber(Node):

    def __init__(self):
        super().__init__('computer_subscriber')
        self.subscription = self.create_subscription(
            Int16,
            '/romi',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        self.get_logger().info('I heard: "%s"' % msg.data)


def main(args=None):
    rclpy.init(args=args)

    computer_subsciber = ComputerSubscriber()

    rclpy.spin(computer_subsciber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    computer_subsciber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
