import motor
import car_dir
import time

motor.setup(busnum=1)
car_dir.setup()
car_dir.home()
car_dir.test()

t = time.time()
while time.time() < t + 5:
    motor.setSpeed(50)
    motor.motor0('True')
    motor.motor1('True')
motor.stop()