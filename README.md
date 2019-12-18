# Obstacle_avoidance_mobile_robot_Microsoft_kinect

* This project shows how to implement the obstacle avoidance for mobile robot using Microsooft Kinect and Raspberry Pi

* First step is to install the freenect driver for microsoft Kinect 
* You can install this driver from the following link

# Step 1 Install Freenect Driver
https://gist.github.com/MaxConners/8b4630c767aeb4a0b324ea4070c3db9d

* Second step is to install opencv on Raspberry Pi

# Step 2 Install opencv 

https://www.pyimagesearch.com/2017/09/04/raspbian-stretch-install-opencv-3-python-on-your-raspberry-pi/

* Next step is to set the motor pins to GPIO of the Raspberry Pi 

* Connect the pins to GPIO Accordingly.

* Mobile robot used for this project had two wheels hence change it accordingly.

* Change the depth range also according to your desired task.

* This method takes into consideration the average depth of the ROI (Region of interest).

* The paper of this project you can found on

*https://ieeexplore.ieee.org/document/8389347*

Implementation

`$ python obstacle.py`
