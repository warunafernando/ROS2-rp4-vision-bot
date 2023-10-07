import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16
import RPi.GPIO as GPIO
from geometry_msgs.msg import Twist
from vision_rpl_bot.a_star import AStar
a_star = AStar()
import time


class RomiSubscriber(Node):

    def __init__(self):
        super().__init__('cmd_romi_subscriber')
        self.subscription = self.create_subscription(Twist,'cmd_vel',self.cmd_to_pwm_callback,10)
        #self.subscription = self.create_subscription(Int16, '/romi', self.listener_callback, 10)
        #self.subscription = self.create_subscription(, 'joy', self.cmd_to_color_callback, 10)
 
        
 
    
    def cmd_to_pwm_callback(self, msg):
        mx = int(msg.linear.x*100*400/70)
        mz = int(msg.angular.z*100*400/40)
        #print(mx,mz)
      
        a_star.motors(mx,mz)
        
    def cmd_to_color_callback(self, msg):
        print(msg)
        
    #def listener_callback(self, msg):
        #self.get_logger().info('I heard: "%s"' % msg.data)
        
        


def main(args=None):
    rclpy.init(args=args)

    romi_subscriber = RomiSubscriber()

    rclpy.spin(romi_subscriber)

    romi_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
