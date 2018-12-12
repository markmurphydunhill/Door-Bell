#import libraries
import RPi.GPIO as GPIO
import time
from time import sleep

import pygame
from pygame import mixer

from wia import Wia
from picamera import PiCamera

pygame.init()
pygame.mixer.init()
mysound = mixer.Sound("SonnetteHaute.wav")

GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_UP)

wia = Wia()
wia.access_token='d_sk_wi9s8K9wVwuO812oUc9QecOk'
camera = PiCamera()

while True:
	input_state = GPIO.input(25)
	if input_state == False:
        	print('Button Pressed')
        	mysound.play()
		## Start up PiCam
		camera.start_preview()
		## sleep for a few seconds to let camera focus/adjust to light
		time.sleep(5)
		## Capture photo
		camera.capture('/home/pi/image.jpg')
		## Stop the PiCam
		camera.stop_preview()
		## Publish "photo" event to Wia. Include the photo file.
		result = wia.Event.publish(name='photo', file=open('/home/pi/image.jpg', 'rb'))
		wia.Event.publish(name='doorbell', data='Ding, Dong !')
	time.sleep(0.5)
