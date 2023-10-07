import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16
import RPi.GPIO as GPIO
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy
from vision_rpl_bot.a_star import AStar
a_star = AStar()
import time


class RomiSubscriber(Node):

    def __init__(self):
        super().__init__('cmd_romi_subscriber')
        self.subscription = self.create_subscription(Joy, 'joy', self.cmd_to_romi_callback, 10)
 
        
    def cmd_to_romi_callback(self, msg):
        #print(msg.buttons)
        #print(msg.axes)
        mx = int(msg.axes[1]*400)
        mz = int(msg.axes[0]*400)
        print(mx,mz)
        a_star.motors(mx,mz)
        a_star.leds(msg.buttons[1],msg.buttons[3],msg.buttons[0])
        


def main(args=None):
    rclpy.init(args=args)

    romi_subscriber = RomiSubscriber()

    rclpy.spin(romi_subscriber)

    romi_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
