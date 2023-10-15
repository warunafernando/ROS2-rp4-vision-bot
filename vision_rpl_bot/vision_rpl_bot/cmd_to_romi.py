import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16
from sensor_msgs.msg import Joy
from vision_rpl_bot.a_star import AStar
a_star = AStar()
import time



class RomiSubscriber(Node):

    def __init__(self):
        super().__init__('cmd_romi_subscriber')
        self.subscription = self.create_subscription(Joy, 'joy', self.cmd_to_romi_callback, 10)

 
        
    def cmd_to_romi_callback(self, msg):
        mx = int(msg.axes[1]*400)
        mz = int(msg.axes[0]*400)
        redButton = (msg.buttons[0])
        orangeButton = (msg.buttons[3])
        blueButton = (msg.buttons[2])
        greenButton = (msg.buttons[1])
        a_star.leds(redButton, greenButton, orangeButton)
        print(mx,mz)
        a_star.motors(mx+mz,mx-mz)
        


def main(args=None):
    rclpy.init(args=args)
    

    romi_subscriber = RomiSubscriber()

    rclpy.spin(romi_subscriber)

    romi_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
