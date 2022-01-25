import time
import picamera


with picamera.PiCamera() as camera:
	print("taking taking taking . . .")
	camera.resolution = (1024, 768)
	camera.start_preview()
	time.sleep(2)
	camera.capture('foo.jpg')
	print("done!")
