import rclpy
from rclpy.node import Node

#from std_msgs.msg import Int16
from std_msgs.msg import Int16MultiArray
from array import array


class ComputerSubscriber(Node):

    def __init__(self):
        super().__init__('computer_subscriber')
        self.subscription = self.create_subscription(
            Int16MultiArray,
            '/romi',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning
        

    def listener_callback(self, msg):
        try:
            data1 = msg.data[0]
            data2 = msg.data[1]
            data3 = msg.data[2]
            print(data1, data2, data3)
        except:
            print("Empty array")
        #self.get_logger().info('I heard: "%s"' % msg.data)
        


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
