import motor

motor.setup(busnum=1)

while True:
    motor.setSpeed(50)
    motor.motor0(True)
    motor.motor1(True)