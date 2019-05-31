import motor
import car_dir
import time



motor.setup(busnum=1)
car_dir.setup()

motor.setSpeed(50)
motor.motor0('True')
motor.motor1('True')

def forward(seconds):
    car_dir.home()
    t = time.time()
    while t + seconds > time.time():
        pass

for _ in range(3):
    for __ in range(2):
        forward(3)
        car_dir.turn_left()
        while t + 6.2727272 > time.time():
            pass
        car_dir.home()

motor.stop()
