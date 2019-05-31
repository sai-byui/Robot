import motor
import car_dir
import time

motor.setup(busnum=1)
car_dir.setup()

motor.setSpeed(50)
motor.motor0('True')
motor.motor1('True')

for _ in range(3):
    for __ in range(2):
        t = time.time()
        while t + 3 > time.time():
            pass
        car_dir.turn_left()
        while t + 6 > time.time():
            pass
        car_dir.home()

motor.stop()