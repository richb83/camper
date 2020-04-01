#! /usr/bin/python3

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(29,GPIO.OUT)
GPIO.setup(31,GPIO.OUT)
GPIO.setup(32,GPIO.OUT)
GPIO.setup(33,GPIO.OUT)

GPIO.output(29,GPIO.HIGH)
GPIO.output(31,GPIO.HIGH)
GPIO.output(32,GPIO.HIGH)
GPIO.output(33,GPIO.HIGH)


GPIO.output(29,GPIO.LOW)
time.sleep(3)
GPIO.output(31,GPIO.LOW)
time.sleep(3)
GPIO.output(32,GPIO.LOW)
time.sleep(3)
GPIO.output(33,GPIO.LOW)



time.sleep(15)

GPIO.cleanup()
