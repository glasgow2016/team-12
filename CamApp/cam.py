'''THIS IS A camera streaming script, that uses the camera of a Raspberry Pi.'''

#!/usr/bin/python

#import the SimpleCV and py_gmailer  libraries
from SimpleCV import *

#initialize the camer
cam = Camera()
#set a streaming variable to stream webcam online
streaming = JpegStreamer("0.0.0.0:1212")

#create a loop that constantly grabs new images from the webcam
while True:
	#send the current image to the webcam stream
	img02.save(streaming)
