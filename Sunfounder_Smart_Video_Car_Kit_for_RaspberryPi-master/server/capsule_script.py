import car
import time

c = car.Car()

c.forward()

for _ in range(3):
    for __ in range(2):
        time.sleep(3)
        c.turn_left()
        time.sleep(3.27272727)
        c.straight()

c.stop()
