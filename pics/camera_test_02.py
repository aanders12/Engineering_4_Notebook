import time
import picamera

with picamera.PiCamera() as camera:
	print("taking, taking, taking ...")
	camera.resolution = (640, 480)
	camera.start_preview()
	time.sleep(2)
	camera.capture("okay.jpg")
	camera.image_effect = 'negative'
	camera.resolution = (640, 480)
	camera.start_preview()
	time.sleep(2)
	camera.capture("workneg.jpg")
	camera.image_effect = 'film'
	camera.resolution = (640,480)
	camera.start_preview()
	time.sleep(2)
	camera.capture("film.jpg")
	camera.image_effect = 'blur'
	camera.resolution = (640, 480)
	camera.start_preview()
	time.sleep(2)
	camera.capture("blurimage.jpg")
	camera.image_effect = 'saturation'
	camera.resolution = (640, 480)
	camera.start_preview()
	time.sleep(2)
	camera.capture("saturated.jpg")	
	print("done!")
