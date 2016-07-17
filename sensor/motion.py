###############################
# Application: Motion Sensor  #
# Using: GPIO 12 (BCM mode)   #
###############################
 
import RPi.GPIO as GPIO
import time, datetime

# GPIO 12 for the motion sensor (BCM) 
PIR = 12

# Flag for motions sensor 
pirVal = False                          # we start, assuming no motion detected

# GPIO Setup  
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR, GPIO.IN)

# Constants
dateString = '%Y/%m/%d %H:%M:%S';
# Start routine
print 'Starting application: ',datetime.datetime.now().strftime(dateString),'\n';
 
while True:
	pirVal = GPIO.input(PIR)            # read input value
	if (pirVal == True):                # check if the input is HIGH
		currentTime = datetime.datetime.now().strftime(dateString);
		print "Motion Detetcted on sensor at:",currentTime;
		time.sleep(1);
		
