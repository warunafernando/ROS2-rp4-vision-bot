import rclpy
from rclpy.node import Node

from std_msgs.msg import Int16MultiArray
from vision_rpl_bot.a_star import AStar
a_star = AStar()

class RomiPublisher(Node):

    def __init__(self):
        super().__init__('romi_publisher')
        self.publisher_ = self.create_publisher(Int16MultiArray, '/romi', 10)
        timer_period = 0.1  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.iterator = 0

    def timer_callback(self):
        voltage = (a_star.read_battery_millivolts()[0])
        encoder=a_star.read_encoders()
        encoder_r=c=encoder[0]
        encoder_l=c=encoder[1]
    
        print(encoder)
        #print(voltage)
        msg = Int16MultiArray()
        if (voltage > 0 and voltage < 10000):
            data_to_send=[voltage, encoder_l, encoder_r]
            msg.data = data_to_send # self.iterator

            
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)
        #self.iterator += 1
        


def main(args=None):
    rclpy.init(args=args)

    romi_publisher = RomiPublisher()

    rclpy.spin(romi_publisher)

    # Destroy    node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    romi_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()