import rclpy
from rclpy.node import Node

from std_msgs.msg import Int16
from vision_rpl_bot.a_star import AStar
a_star = AStar()

class RomiPublisher(Node):

    def __init__(self):
        super().__init__('romi_publisher')
        self.publisher_ = self.create_publisher(Int16, '/romi', 10)
        timer_period = 0.1  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.iterator = 0

    def timer_callback(self):
        voltage = ((a_star.read_battery_millivolts()[0]))
        #print(voltage)
        msg = Int16()
        if (voltage > 0 and voltage < 10000):
            
            msg.data = (voltage) # self.iterator

            
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)
        #self.iterator += 1
        


def main(args=None):
    rclpy.init(args=args)

    romi_publisher = RomiPublisher()

    rclpy.spin(romi_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    romi_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()