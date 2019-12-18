#import the necessary modules
import freenect
import cv2
import numpy as np
import RPi.GPIO as GPIO
from time import sleep
#import scipy
#function to get RGB image from kinect
def get_video():
	array,_ = freenect.sync_get_video()
	array = cv2.cvtColor(array,cv2.COLOR_RGB2BGR)
   	return array
#function to get depth image from kinect
def get_depth():
	array,_ = freenect.sync_get_depth()
	#array = array.astype(np.uint16)
	return array

if __name__ == "__main__":

	#_min = 2047
	GPIO.setmode(GPIO.BOARD)
	Motor1A = 16
	Motor1B = 18
	Motor1E = 22
	GPIO.setup(Motor1A,GPIO.OUT)
	GPIO.setup(Motor1B,GPIO.OUT)
	GPIO.setup(Motor1E,GPIO.OUT)
	GPIO.output(Motor1A,GPIO.HIGH)
	GPIO.output(Motor1B,GPIO.LOW)
	GPIO.output(Motor1E,GPIO.LOW)
while(1):

	depth = get_depth()
	depth_roi = depth[depth.shape[0]/3:depth.shape[0]*2/3,depth.shape[1]/3:depth.shape[1]*2/3]
	#depth_roi_img = scipy.misc.toimage(depth_roi)
	#cv2.imshow('ROI',np.divide(depth_roi,2047))
	depth_min_roi = depth_roi.flatten()[depth_roi.argmin()]
	avg_depth = int(depth_min_roi)
	print(avg_depth)
	#print(depth[depth.shape[0]/2][depth.shape[1]/2])
	if(depth_min_roi < 450 ):
		print ("You are too close")
		GPIO.output(Motor1E,GPIO.LOW)
		elif(depth_min_roi > 900):
		print("Out of range")
		GPIO.output(Motor1E,GPIO.LOW)
	else:
		print("You are far away")
		GPIO.output(Motor1E,GPIO.HIGH)