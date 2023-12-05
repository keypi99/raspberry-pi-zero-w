import RPi.GPIO as GPIO
import time

#GPIO.cleanup()
commento=''
try:
      GPIO.setmode(GPIO.BCM)

      PIN_TRIGGER = 15
      PIN_ECHO = 2

      GPIO.setup(PIN_TRIGGER, GPIO.OUT)
      GPIO.setup(PIN_ECHO, GPIO.IN)

      GPIO.output(PIN_TRIGGER, 1)


      if GPIO.input(PIN_ECHO):
            commento='Bagnato'
      else:
            commento='Asciutto'

      print(commento)
      
finally:
      GPIO.cleanup()