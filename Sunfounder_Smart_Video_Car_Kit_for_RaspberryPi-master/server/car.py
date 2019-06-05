import motor
import car_dir
import time

class Car:
    def __init__(self):
        motor.setup(busnum=1)
        car_dir.setup()

    def forward(self, speed=50):
        """Will cause the car to start moving forward.
        Car will not stop until stop() is called"""
        motor.setSpeed(speed)
        motor.motor0('True')
        motor.motor1('True')

    def backward(self, speed=50):
        """Similar to forward()"""
        motor.setSpeed(speed)
        motor.motor0('False')
        motor.motor1('False')

    def turn_left(self):
        """Front wheels will turn left, regardless of whether it
        is moving or not."""
        car_dir.turn_left()

    def turn_right(self):
        """Similar to turn_left()"""
        car_dir.turn_right()

    def stop(self):
        """Stops the forward or backward motion of the car"""
        motor.stop()

    def straight(self):
        """Turns the front wheels to face forward"""
        car_dir.home()

    def turn(self, amt):
        car_dir.turn_car(amt)