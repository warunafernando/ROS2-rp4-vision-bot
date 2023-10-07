import rclpy
from rclpy.node import Node
import RPi.GPIO as GPIO
from geometry_msgs.msg import Twist
from vision_rpl_bot.a_star import AStar
a_star = AStar()
import time


class RomiSubscriber(Node):

    def __init__(self):
        super().__init__('cmd_romi_subscriber')
        self.subscription = self.create_subscription(Twist,'cmd_vel',self.cmd_to_pwm_callback,10)
        
 
    
    def cmd_to_pwm_callback(self, msg):
        mx = int(msg.linear.x*100*400/70)
        mz = int(msg.angular.z*100*400/40)
        print(mx,mz)
      
        a_star.motors(mx,mz)
        
        
        


def main(args=None):
    rclpy.init(args=args)

    romi_subscriber = RomiSubscriber()

    rclpy.spin(romi_subscriber)

    romi_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
