#!/usr/bin/python
import time
#for gpio pins
import RPi.GPIO as GPIO

#Communication library
import pika

#Input of messages
import sys

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)
GPIO.setup(18, GPIO.IN)
GPIO.setup(27, GPIO.IN)
GPIO.setup(22, GPIO.IN)

def send_message(message):
	connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
	channel = connection.channel()

	channel.exchange_declare(exchange='christmas', type='fanout')

	#message is passed in
	channel.basic_publish(exchange='christmas',
			      routing_key='',
			      body = message)

	print(" [x] Sent message: %s" % message)
	connection.close()



def main():
	#Initilize Message to be just the "-" demarcation character
	msg = '-'	
	print('starting button test')
	'''
	#Grab All of the command line args
	#This does not check anything, just passes them straight through
	for i in range(1,len(sys.argv)):
		print("%d cmd: %r " %(i, sys.argv[i]))	
		#Append arguments to message with a "-" character inbetween everything
		msg = msg+sys.argv[i]+'-'
	
	print("Constructed Message: ^%s^" %msg)	
	'''

	while(1):
		if GPIO.input(17):
			print('0')
			send_message('-2-200-0-0-')
			time.sleep(1)
		if GPIO.input(18):
			print('1')
			send_message('-2-0-200-0-')
			time.sleep(1)
		if GPIO.input(27):
			print('2')
			send_message('-2-0-0-200-')
			time.sleep(1)
		if GPIO.input(22):
			print('3')
			send_message('-2-200-200-200-')
			time.sleep(1)
	#Send Message to the attached Pi's
	#send_message(msg)

main()
