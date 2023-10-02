import rclpy
from rclpy.node import Node
import RPi.GPIO as GPIO
from geometry_msgs.msg import Twist


class VelocitySubscriber(Node):

    def __init__(self):
        super().__init__('cmd_vel_subscriber')
        self.subscription = self.create_subscription(Twist,'cmd_vel',self.cmd_to_pwm_callback,10)
        motor_a=16
        motor_b=20
        motor_en=21
        GPIO.setmode(GPIO.BCM)
        self.mr_a=motor_a
        self.mr_b=motor_b
        GPIO.setup(motor_a, GPIO.OUT)
        GPIO.setup(motor_b, GPIO.OUT)
        GPIO.setup(motor_en, GPIO.OUT)

        self.pwm=GPIO.PWM(motor_en,1000)
        self.pwm.start(25)
    def cmd_to_pwm_callback(self, msg):
        wheel_vel=(msg.linear.x + msg.angular.z)/2
        
        speed=abs(int(wheel_vel*280))
        print(speed)
        self.pwm.ChangeDutyCycle(speed)
        GPIO.output(self.mr_a, wheel_vel > 0)
        GPIO.output(self.mr_b, wheel_vel < 0)

def main(args=None):
    rclpy.init(args=args)

    velocity_subscriber = VelocitySubscriber()

    rclpy.spin(velocity_subscriber)

    velocity_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
