#!/bin/python3
import serial
from PIL import ImageEnhance
# windows
from PIL import ImageGrab
# linux
#from mss.linux import MSS as mss

def screenshot():
	# windows
	img = ImageGrab.grab()

	return img

def average(img, LOW_THRESH, HIGH_THRESH, MAX_BRIGHTNESS):
	pixels = list(img.getdata())
	dark_pixels = 0
	bright_pixels = 0

	r = 0
	g = 0
	b = 0

	for red, green, blue in pixels:
		if red < LOW_THRESH and green < LOW_THRESH and blue < LOW_THRESH:
			dark_pixels += 1

		# might do some experimentation on light pixels
		if red > HIGH_THRESH and green > HIGH_THRESH and red > HIGH_THRESH:
			bright_pixels += 1
			# maybe do a pass so there isnt too much 'white'

		r += red
		g += green
		b += blue

	n = len(pixels)

	# faster than round and not too big of a deal
	r_avg = r // n
	g_avg = g // n
	b_avg = b // n

	# / n - bright_pixels
	# i dont  think its bright enough
	# have to test the min brightness on the LEDs if brightness > max brightness, brightness = max brightness

	brightness = round((dark_pixels / n * MAX_BRIGHTNESS))

	return [r_avg, g_avg, b_avg, brightness]

def send(ser, output):
	for color in output:
		#print(bytes(color))
		ser.write(bytes(color))

def setup_serial():
	ser = serial.Serial('COM3', 9600)
	return ser


ser = setup_serial()
# should close port as well somehow

while True:
	# windows
	#img = ImageGrab.grab()
	img = screenshot()
	# linux
	#sct = mss()

	#for filename in sct.save():
	#    print(filename)

	output = average(img, 10, 240, 255)
	print(output)
	#send(output)

