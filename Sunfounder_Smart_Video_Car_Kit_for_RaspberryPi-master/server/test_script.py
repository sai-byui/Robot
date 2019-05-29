import motor
import car_dir
import time

motor.setup(busnum=1)
car_dir.setup()

motor.setSpeed(50)
motor.motor0('True')
motor.motor1('True')
t = time.time()

while time.time() < t + 1:
    pass

car_dir.turn_left()

while time.time() < t + 1.5:
    pass

car_dir.home()

while time.time() < t + 2.5:
    pass

motor.stop()