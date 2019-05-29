import motor
import time

motor.setup(busnum=1)
t = time.time()
while time.time < t + 5:
    motor.setSpeed(50)
    motor.motor0('True')
    motor.motor1('True')
motor.stop()