import RPi.GPIO as GPIO
import time

motor_a=16
motor_b=20
motor_en=21

GPIO.setmode(GPIO.BCM)

GPIO.setup(motor_a, GPIO.OUT)
GPIO.setup(motor_b, GPIO.OUT)
GPIO.setup(motor_en, GPIO.OUT)

pwm=GPIO.PWM(motor_en,1000)

pwm.start(25)

def forward(second):
    print("moving forward")
    GPIO.output(motor_a, GPIO.HIGH)
    GPIO.output(motor_b, GPIO.LOW)
    time.sleep(second)

def backward(second):
    print("moving backward")
    GPIO.output(motor_a, GPIO.LOW)
    GPIO.output(motor_b, GPIO.HIGH)
    time.sleep(second)
    
def stop():
    print("stop")
    pwm.ChangeDutyCycle(0)
    
def exit():
    GPIO.cleanup()
    
def main():
    forward(2)
    backward(2)
    stop()
    exit()
    

if __name__=='__main__':
    main()