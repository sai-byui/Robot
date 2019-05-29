import motor
import car_dir
import time

motor.setup(busnum=1)
pwm = input("What pwm to test: (q to quit): ")
while pwm != 'q':
    car_dir.setup(pwm_default=pwm)
    car_dir.home()
    pwm = input("What pwm to test: (q to quit): ")

# t = time.time()
# while time.time() < t + 5:
#     motor.setSpeed(50)
#     motor.motor0('True')
#     motor.motor1('True')
# motor.stop()