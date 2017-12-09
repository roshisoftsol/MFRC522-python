#!/usr/bin/env python
# -*- coding: utf8 -*-

import RPi.GPIO as GPIO
import SimpleMFRC522
import signal

continue_reading = True

# Capture SIGINT for cleanup when the script is aborted
def end_read(signal,frame):
	global continue_reading
	print "Ctrl+C captured, ending read."
	continue_reading = False
	GPIO.cleanup()

# Hook the SIGINT
signal.signal(signal.SIGINT, end_read)

# Create an object of the class MFRC522
reader = SimpleMFRC522.SimpleMFRC522()

# Welcome message
print "Welcome to the MFRC522 data read example"
print "Press Ctrl-C to stop."

# This loop keeps checking for chips. If one is near it will get the UID and authenticate
try:
	while continue_reading:
		id, text = reader.read()
		print(id)
		print(text)
finally:
	GPIO.cleanup()