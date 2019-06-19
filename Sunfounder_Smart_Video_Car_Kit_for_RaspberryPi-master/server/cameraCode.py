from picamera import PiCamera
from time import sleep, time
import datetime

camera = PiCamera()
camera.vflip = True
camera.hflip = True
camera.start_preview()

for i in range(100):
	sleep(.25)
	camera.capture('home/pi/Pictures/image%s.jpg' % datetime.datetime.now())
camera.stop_preview()
